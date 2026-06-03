import sqlite3
from datetime import datetime, timezone
from typing import List, Optional

from domain.entities import Figurinha
from infra.database import connection
from repository.figurinha_repo import FigurinhaRepository


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _to_figurinha(row: sqlite3.Row) -> Figurinha:
    return Figurinha(**dict(row))


class SQLiteFigurinhaRepository(FigurinhaRepository):
    def save(self, figurinha: Figurinha) -> Figurinha:
        created_at = figurinha.created_at or _now()
        updated_at = figurinha.updated_at or created_at
        with connection() as conn:
            cursor = conn.execute(
                "INSERT INTO figurinha (numero, tipo, posicao, created_at, updated_at) "
                "VALUES (?, ?, ?, ?, ?)",
                (
                    figurinha.numero,
                    figurinha.tipo.value,
                    figurinha.posicao.value,
                    created_at.isoformat(),
                    updated_at.isoformat(),
                ),
            )
            new_id = cursor.lastrowid
        return figurinha.model_copy(
            update={"id": new_id, "created_at": created_at, "updated_at": updated_at}
        )

    def find_by_id(self, id: int) -> Optional[Figurinha]:
        with connection() as conn:
            row = conn.execute("SELECT * FROM figurinha WHERE id = ?", (id,)).fetchone()
        return _to_figurinha(row) if row else None

    def find_all(
        self,
        posicao: Optional[str] = None,
        tipo: Optional[str] = None,
    ) -> List[Figurinha]:
        query = "SELECT * FROM figurinha"
        clauses: List[str] = []
        params: List[str] = []
        if posicao:
            clauses.append("posicao = ?")
            params.append(posicao)
        if tipo:
            clauses.append("tipo = ?")
            params.append(tipo)
        if clauses:
            query += " WHERE " + " AND ".join(clauses)
        query += " ORDER BY id"

        with connection() as conn:
            rows = conn.execute(query, params).fetchall()
        return [_to_figurinha(row) for row in rows]

    def update(self, figurinha: Figurinha) -> Optional[Figurinha]:
        with connection() as conn:
            cursor = conn.execute(
                "UPDATE figurinha "
                "SET numero = ?, tipo = ?, posicao = ?, updated_at = ? "
                "WHERE id = ?",
                (
                    figurinha.numero,
                    figurinha.tipo.value,
                    figurinha.posicao.value,
                    _now().isoformat(),
                    figurinha.id,
                ),
            )
            if cursor.rowcount == 0:
                return None
        return self.find_by_id(figurinha.id)

    def delete(self, id: int) -> bool:
        with connection() as conn:
            cursor = conn.execute("DELETE FROM figurinha WHERE id = ?", (id,))
            return cursor.rowcount > 0

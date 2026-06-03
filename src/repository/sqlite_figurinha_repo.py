from datetime import datetime, timezone

from domain.entities import Figurinha
from infra.database import connection
from repository.figurinha_repo import FigurinhaRepository


class SQLiteFigurinhaRepository(FigurinhaRepository):
    def save(self, figurinha):
        now = datetime.now(timezone.utc)
        with connection() as conn:
            cursor = conn.execute(
                "INSERT INTO figurinha (numero, tipo, posicao, created_at, updated_at) "
                "VALUES (?, ?, ?, ?, ?)",
                (
                    figurinha.numero,
                    figurinha.tipo.value,
                    figurinha.posicao.value,
                    now.isoformat(),
                    now.isoformat(),
                ),
            )
            new_id = cursor.lastrowid
        return figurinha.model_copy(
            update={"id": new_id, "created_at": now, "updated_at": now}
        )

    def find_by_id(self, id):
        with connection() as conn:
            row = conn.execute("SELECT * FROM figurinha WHERE id = ?", (id,)).fetchone()
        if not row:
            return None
        return Figurinha(**dict(row))

    def find_all(self, posicao=None, tipo=None):
        query = "SELECT * FROM figurinha"
        clauses = []
        params = []
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
        return [Figurinha(**dict(row)) for row in rows]

    def update(self, figurinha):
        now = datetime.now(timezone.utc)
        with connection() as conn:
            cursor = conn.execute(
                "UPDATE figurinha "
                "SET numero = ?, tipo = ?, posicao = ?, updated_at = ? "
                "WHERE id = ?",
                (
                    figurinha.numero,
                    figurinha.tipo.value,
                    figurinha.posicao.value,
                    now.isoformat(),
                    figurinha.id,
                ),
            )
            if cursor.rowcount == 0:
                return None
        return self.find_by_id(figurinha.id)

    def delete(self, id):
        with connection() as conn:
            cursor = conn.execute("DELETE FROM figurinha WHERE id = ?", (id,))
            return cursor.rowcount > 0

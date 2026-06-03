# services/figurinha_service.py

from datetime import datetime, timezone
from typing import List, Optional

from domain.entities.figurinha import Figurinha


# exceções de Domínio para o Handler capturar depois
class ValidationError(Exception):
    pass


class NotFoundError(Exception):
    pass


class FigurinhaService:
    def __init__(self, repository):
        self.repository = repository
        self.tipos_validos = ["comum", "brilhante", "legends_ouro", "legends_bronze"]
        self.posicoes_validas = ["Goleiro", "Zagueiro", "Meio-campista", "Atacante"]

    def create_figurinha(self, dados_requisicao: dict) -> Figurinha:
        # campos obrigatórios
        if (
            not dados_requisicao.get("numero")
            or not dados_requisicao.get("tipo")
            or not dados_requisicao.get("posicao")
        ):
            raise ValidationError(
                "Todos os campos (numero, tipo, posicao) são obrigatórios."
            )

        # categoria deve ser um dos valores válidos
        tipo = dados_requisicao["tipo"]
        posicao = dados_requisicao["posicao"]

        if tipo not in self.tipos_validos:
            raise ValidationError(
                f"Tipo inválido. Deve ser um de: {self.tipos_validos}"
            )
        if posicao not in self.posicoes_validas:
            raise ValidationError(
                f"Posição inválida. Deve ser uma de: {self.posicoes_validas}"
            )

        # preenchida automaticamente
        horario_atual = datetime.now(timezone.utc)

        nova_figurinha = Figurinha(
            id=0,
            numero=dados_requisicao["numero"],
            tipo=tipo,
            posicao=posicao,
            created_at=horario_atual,
            updated_at=horario_atual,
        )

        return self.repository.save(nova_figurinha)

    def get_todas_figurinhas(
        self, filtro_posicao: Optional[str] = None, filtro_tipo: Optional[str] = None
    ) -> List[Figurinha]:
        # validar a categoria tanto no filtro da listagem
        if filtro_posicao and filtro_posicao not in self.posicoes_validas:
            raise ValidationError(
                f"Filtro de posição inválido. Deve ser uma de: {self.posicoes_validas}"
            )

        if filtro_tipo and filtro_tipo not in self.tipos_validos:
            raise ValidationError(
                f"Filtro de tipo inválido. Deve ser um de: {self.tipos_validos}"
            )

        return self.repository.find_all(posicao=filtro_posicao, tipo=filtro_tipo)

    def get_figurinha_por_id(self, figurinha_id: int) -> Figurinha:
        figurinha = self.repository.find_by_id(figurinha_id)
        # ao buscar ID inexistente, retornar erro para gerar o 404
        if not figurinha:
            raise NotFoundError("figurinha não encontrado")
        return figurinha

    def put_figurinha(self, figurinha_id: int, dados_atualizacao: dict) -> Figurinha:
        # ao buscar ou atualizar um ID inexistente, estourar NotFoundError
        figurinha_existente = self.repository.find_by_id(figurinha_id)
        if not figurinha_existente:
            raise NotFoundError("figurinha não encontrado")

        if (
            not dados_atualizacao.get("numero")
            or not dados_atualizacao.get("tipo")
            or not dados_atualizacao.get("posicao")
        ):
            raise ValidationError(
                "Todos os campos (numero, tipo, posicao) são obrigatórios."
            )

        # cria a entidade com os novos dados enviados
        figurinha_atualizada = Figurinha(
            id=figurinha_id,
            numero=dados_atualizacao["numero"],
            tipo=dados_atualizacao["tipo"],
            posicao=dados_atualizacao["posicao"],
            created_at=dados_atualizacao.get("created_at"),
            updated_at=dados_atualizacao.get("updated_at"),
        )

        return self.repository.update(figurinha_atualizada)

    def delete_figurinha(self, figurinha_id: int) -> None:
        self.get_figurinha_por_id(figurinha_id)
        self.repository.delete(figurinha_id)

"""empty message

Revision ID: 8d7aeb6ba8cf
Revises: 76cbab82c903
Create Date: 2021-09-02 08:37:27.223543

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8d7aeb6ba8cf'
down_revision = '76cbab82c903'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entregas', sa.Column('concluida', sa.Boolean(), nullable=True))
    op.alter_column('entregas', 'destino',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('equipamentos', 'nome',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('pedidos', 'valor_total',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('pedidos_itens', 'preco_data',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('pontos_de_venda', 'nome',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.create_unique_constraint(None, 'pontos_de_venda', ['nome'])
    op.alter_column('produtos', 'nome',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('tipo_ponto_venda', 'nome',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.create_unique_constraint(None, 'tipo_ponto_venda', ['nome'])
    op.alter_column('unidades', 'nome',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.create_unique_constraint(None, 'unidades', ['nome'])
    op.alter_column('usuarios', 'nome_usuario',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.create_unique_constraint(None, 'usuarios', ['nome_usuario'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'usuarios', type_='unique')
    op.alter_column('usuarios', 'nome_usuario',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_constraint(None, 'unidades', type_='unique')
    op.alter_column('unidades', 'nome',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.drop_constraint(None, 'tipo_ponto_venda', type_='unique')
    op.alter_column('tipo_ponto_venda', 'nome',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('produtos', 'nome',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.drop_constraint(None, 'pontos_de_venda', type_='unique')
    op.alter_column('pontos_de_venda', 'nome',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('pedidos_itens', 'preco_data',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('pedidos', 'valor_total',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('equipamentos', 'nome',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('entregas', 'destino',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.drop_column('entregas', 'concluida')
    # ### end Alembic commands ###

from app.extensions import db


class UserModel(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True, index=True)
    senha_hash = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(30), nullable=True)
    endereco = db.Column(db.String(255), nullable=True)
    papel = db.Column(db.String(50), nullable=False, default="empreendedora")
    ativo = db.Column(db.Boolean, nullable=False, default=True)
    criado_em = db.Column(db.String(50), nullable=False)

    produtos = db.relationship("ProductModel", back_populates="usuario", cascade="all, delete-orphan")
    pedidos = db.relationship("OrderModel", back_populates="usuario", cascade="all, delete-orphan")
    mentorias = db.relationship("MentoriaModel", back_populates="usuario", cascade="all, delete-orphan")
    trilhas = db.relationship("TrailModel", back_populates="usuario", cascade="all, delete-orphan")


class ProductModel(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(40), nullable=False, default="ativo")

    usuario = db.relationship("UserModel", back_populates="produtos")
    itens_pedido = db.relationship("OrderItemModel", back_populates="produto")
    anuncios = db.relationship("AnnouncementModel", back_populates="produto", cascade="all, delete-orphan")


class OrderModel(db.Model):
    __tablename__ = "pedidos"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    endereco_entrega = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(40), nullable=False, default="criado")
    data_criacao = db.Column(db.String(50), nullable=False)
    valor_total = db.Column(db.Float, nullable=False, default=0.0)

    usuario = db.relationship("UserModel", back_populates="pedidos")
    itens = db.relationship("OrderItemModel", back_populates="pedido", cascade="all, delete-orphan")
    invoices = db.relationship("InvoiceModel", back_populates="pedido", cascade="all, delete-orphan")


class OrderItemModel(db.Model):
    __tablename__ = "pedido_itens"

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey("pedidos.id"), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey("produtos.id"), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)

    pedido = db.relationship("OrderModel", back_populates="itens")
    produto = db.relationship("ProductModel", back_populates="itens_pedido")


class MentoriaModel(db.Model):
    __tablename__ = "mentorias"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    mentora = db.Column(db.String(120), nullable=False)
    data_hora = db.Column(db.String(50), nullable=False)
    tema = db.Column(db.String(120), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(40), nullable=False, default="agendada")
    criado_em = db.Column(db.String(50), nullable=False)

    usuario = db.relationship("UserModel", back_populates="mentorias")
    avaliacoes = db.relationship("MentoriaReviewModel", back_populates="mentoria", cascade="all, delete-orphan")


class ContentModel(db.Model):
    __tablename__ = "conteudos"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)

    trilha_itens = db.relationship("TrailItemModel", back_populates="conteudo")
    progressos = db.relationship("ContentProgressModel", back_populates="conteudo")


class TrailModel(db.Model):
    __tablename__ = "trilhas"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    tipo = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(40), nullable=False, default="ativa")
    criado_em = db.Column(db.String(50), nullable=False)

    usuario = db.relationship("UserModel", back_populates="trilhas")
    itens = db.relationship("TrailItemModel", back_populates="trilha", cascade="all, delete-orphan")


class TrailItemModel(db.Model):
    __tablename__ = "trilha_itens"

    id = db.Column(db.Integer, primary_key=True)
    trilha_id = db.Column(db.Integer, db.ForeignKey("trilhas.id"), nullable=False)
    conteudo_id = db.Column(db.Integer, db.ForeignKey("conteudos.id"), nullable=False)
    ordem = db.Column(db.Integer, nullable=False)
    obrigatorio = db.Column(db.Boolean, nullable=False, default=True)

    trilha = db.relationship("TrailModel", back_populates="itens")
    conteudo = db.relationship("ContentModel", back_populates="trilha_itens")


class AnnouncementModel(db.Model):
    __tablename__ = "anuncios"

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey("produtos.id"), nullable=False)
    status_anuncio = db.Column(db.String(40), nullable=False, default="rascunho")
    data_publicacao = db.Column(db.String(50), nullable=True)

    produto = db.relationship("ProductModel", back_populates="anuncios")


class MentorAgendaModel(db.Model):
    __tablename__ = "agendas_mentora"

    id = db.Column(db.Integer, primary_key=True)
    mentora_id = db.Column(db.Integer, nullable=False)
    data_hora = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=True)
    disponivel = db.Column(db.Boolean, nullable=False, default=True)


class MentoriaReviewModel(db.Model):
    __tablename__ = "avaliacoes_mentoria"

    id = db.Column(db.Integer, primary_key=True)
    mentoria_id = db.Column(db.Integer, db.ForeignKey("mentorias.id"), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    comentario = db.Column(db.Text, nullable=False)
    data_avaliacao = db.Column(db.String(50), nullable=True)

    mentoria = db.relationship("MentoriaModel", back_populates="avaliacoes")


class AddressModel(db.Model):
    __tablename__ = "enderecos"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(60), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)


class EventMetricModel(db.Model):
    __tablename__ = "metricas_evento"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    event_type = db.Column(db.String(80), nullable=False)
    reference_id = db.Column(db.String(120), nullable=False)
    event_date = db.Column(db.String(50), nullable=False)


class NotificationModel(db.Model):
    __tablename__ = "notificacoes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    channel = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    send_status = db.Column(db.String(40), nullable=False, default="pending")
    send_date = db.Column(db.String(50), nullable=False)


class PartnerModel(db.Model):
    __tablename__ = "parceiros"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    partner_type = db.Column(db.String(80), nullable=False)
    contact = db.Column(db.String(120), nullable=False)

    offers = db.relationship("PartnerOfferModel", back_populates="partner", cascade="all, delete-orphan")


class PartnerOfferModel(db.Model):
    __tablename__ = "ofertas_parceiro"

    id = db.Column(db.Integer, primary_key=True)
    partner_id = db.Column(db.Integer, db.ForeignKey("parceiros.id"), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    criteria_json = db.Column(db.Text, nullable=False)
    enrollment_url = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    partner = db.relationship("PartnerModel", back_populates="offers")


class InvoiceModel(db.Model):
    __tablename__ = "faturas"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("pedidos.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    due_date = db.Column(db.String(50), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    status = db.Column(db.String(40), nullable=False, default="pending")
    issue_date = db.Column(db.String(50), nullable=False)

    pedido = db.relationship("OrderModel", back_populates="invoices")
    pagamentos = db.relationship("PaymentModel", back_populates="invoice", cascade="all, delete-orphan")


class PaymentModel(db.Model):
    __tablename__ = "pagamentos"

    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey("faturas.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    gateway_type = db.Column(db.String(50), nullable=False)
    transaction_gateway = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(40), nullable=False, default="pending")
    payment_date = db.Column(db.String(50), nullable=True)

    invoice = db.relationship("InvoiceModel", back_populates="pagamentos")


class ContentProgressModel(db.Model):
    __tablename__ = "progressos_conteudo"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    conteudo_id = db.Column(db.Integer, db.ForeignKey("conteudos.id"), nullable=False)
    status = db.Column(db.String(40), nullable=False, default="nao_iniciado")
    percentual = db.Column(db.Integer, nullable=False, default=0)
    ultimo_acesso = db.Column(db.String(50), nullable=False)

    conteudo = db.relationship("ContentModel", back_populates="progressos")


class DiagnosisModel(db.Model):
    __tablename__ = "diagnosticos"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    score_first = db.Column(db.Float, nullable=False)
    level = db.Column(db.String(60), nullable=False)
    answers = db.Column(db.JSON, nullable=False)
    date_app = db.Column(db.String(50), nullable=False)
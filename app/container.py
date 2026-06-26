from werkzeug.security import generate_password_hash

from app.controllers.announcement_controller import AnnouncementController
from app.controllers.auth_controller import AuthController
from app.controllers.finance_controller import FinanceController
from app.controllers.learning_ops_controller import LearningOpsController
from app.controllers.mentoria_controller import MentoriaController
from app.controllers.mentoring_ops_controller import MentoringOpsController
from app.controllers.order_controller import OrderController
from app.controllers.partner_controller import PartnerController
from app.controllers.product_controller import ProductController
from app.controllers.support_controller import SupportController
from app.controllers.trilha_controller import TrilhaController
from app.controllers.user_controller import UserController
from app.models.user import User
from app.repositories.sqlite import (
    AddressRepository,
    AnnouncementRepository,
    ContentProgressRepository,
    ConteudoRepository,
    DiagnosisRepository,
    EventMetricRepository,
    InvoiceRepository,
    MentoriaRepository,
    MentoriaReviewRepository,
    MentorAgendaRepository,
    NotificationRepository,
    OrderRepository,
    PartnerOfferRepository,
    PartnerRepository,
    PaymentRepository,
    ProductRepository,
    TrilhaRepository,
    UserRepository,
)
from app.services.announcement_service import AnnouncementService
from app.services.auth_service import AuthService
from app.services.finance_service import FinanceService
from app.services.learning_ops_service import LearningOpsService
from app.services.mentoria_service import MentoriaService
from app.services.mentoring_ops_service import MentoringOpsService
from app.services.order_service import OrderService
from app.services.partner_service import PartnerService
from app.services.product_service import ProductService
from app.services.support_service import SupportService
from app.services.trilha_service import TrilhaService
from app.services.user_service import UserService


class AppContainer:
    def __init__(self) -> None:
        self.user_repository = UserRepository()
        self.product_repository = ProductRepository()
        self.order_repository = OrderRepository()
        self.mentoria_repository = MentoriaRepository()
        self.conteudo_repository = ConteudoRepository()
        self.trilha_repository = TrilhaRepository()
        self.announcement_repository = AnnouncementRepository()
        self.agenda_repository = MentorAgendaRepository()
        self.review_repository = MentoriaReviewRepository()
        self.partner_repository = PartnerRepository()
        self.partner_offer_repository = PartnerOfferRepository()
        self.invoice_repository = InvoiceRepository()
        self.payment_repository = PaymentRepository()
        self.address_repository = AddressRepository()
        self.metric_repository = EventMetricRepository()
        self.notification_repository = NotificationRepository()
        self.progress_repository = ContentProgressRepository()
        self.diagnosis_repository = DiagnosisRepository()

        self.auth_service = AuthService(self.user_repository)
        self.user_service = UserService(self.user_repository)
        self.product_service = ProductService(self.product_repository, self.user_repository)
        self.order_service = OrderService(self.order_repository, self.product_repository, self.user_repository)
        self.mentoria_service = MentoriaService(self.mentoria_repository, self.user_repository)
        self.trilha_service = TrilhaService(self.trilha_repository, self.conteudo_repository, self.user_repository)
        self.announcement_service = AnnouncementService(self.announcement_repository, self.product_repository)
        self.mentoring_ops_service = MentoringOpsService(self.agenda_repository, self.mentoria_repository, self.review_repository, self.user_repository)
        self.partner_service = PartnerService(self.partner_repository, self.partner_offer_repository)
        self.finance_service = FinanceService(self.invoice_repository, self.payment_repository, self.order_repository, self.user_repository)
        self.support_service = SupportService(self.address_repository, self.metric_repository, self.notification_repository, self.user_repository)
        self.learning_ops_service = LearningOpsService(self.progress_repository, self.diagnosis_repository, self.conteudo_repository, self.user_repository)

        self.auth_controller = AuthController(self.auth_service)
        self.user_controller = UserController(self.user_service)
        self.product_controller = ProductController(self.product_service)
        self.order_controller = OrderController(self.order_service)
        self.mentoria_controller = MentoriaController(self.mentoria_service)
        self.trilha_controller = TrilhaController(self.trilha_service)
        self.announcement_controller = AnnouncementController(self.announcement_service)
        self.mentoring_ops_controller = MentoringOpsController(self.mentoring_ops_service)
        self.partner_controller = PartnerController(self.partner_service)
        self.finance_controller = FinanceController(self.finance_service)
        self.support_controller = SupportController(self.support_service)
        self.learning_ops_controller = LearningOpsController(self.learning_ops_service)

    def initialize_data(self) -> None:
        self.conteudo_repository.seed_defaults()
        self._seed_initial_data()

    def _seed_initial_data(self) -> None:
        admin = User(
            nome="Administradora",
            email="admin@empreendamaiselas.com",
            senha_hash=generate_password_hash("admin123"),
            papel="admin",
            telefone="(88) 99999-9999",
            endereco="Polo Lavras da Mangabeira",
        )
        if not self.user_repository.get_by_email(admin.email):
            self.user_repository.create(admin)


container = AppContainer()
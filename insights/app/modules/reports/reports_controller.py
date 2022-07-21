from fastapi import Depends
from fastapi_module import InferringRouter, controller


from modules.authorization.authorization_deps import get_authorized_user
from modules.reports.reports_dtos import Report, Reports
from modules.reports.reports_mapper import ReportsMapper
from modules.reports.reports_service import ReportsService
from modules.users.users_dtos import User


router = InferringRouter(tags=["Reports"])


@controller(router, version=1.1)
class ReportsController:
    reports_service: ReportsService = Depends()
    reports_mapper: ReportsMapper = Depends()

    @router.get("/")
    async def get_reports(self, me: User = Depends(get_authorized_user("reports", "read"))) -> Reports:
        """
        **Get reports**

        `:return: list of reports`
        """
        reports = self.reports_service.get_reports()
        return self.reports_mapper.to_reports(reports)

    @router.get("/{report_id}")
    async def get_report(self, report_id: int, me: User = Depends(get_authorized_user("reports", "read"))) -> Report:
        """
        **Get report**

        `:param report_id: report id`

        `:return: report`
        """
        report = self.reports_service.get_report_by_id(report_id)
        return self.reports_mapper.to_report(report)

from typing import List
from http.client import HTTPException


from modules.reports.reports_models import ReportModel


class ReportsService:
    def get_reports(self) -> List[ReportModel]:
        return ReportModel.all()

    def get_report_by_id(self, id: int) -> ReportModel | HTTPException:
        report = ReportModel.get(id=id)
        
        if report is None:
            raise HTTPException(status_code=404)

        return report

from typing import List


from modules.reports.reports_dtos import Report, Reports
from modules.reports.reports_models import ReportModel


class ReportsMapper:
    def to_report(self, report: ReportModel) -> Report:
        return Report(id=report.id, title=report.title, description=report.description)

    def to_reports(self, reports: List[ReportModel]) -> Reports:
        return Report(reports=[self.to_report(report) for report in reports])

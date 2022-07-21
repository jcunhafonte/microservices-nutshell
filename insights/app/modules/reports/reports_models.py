class ReportModel:
    reports = {
        1: dict(
            id=1,
            title="Monthly Financial Transactions",
            description="Monthly financial transactions for the current month",
        ),
        2: dict(
            id=2,
            title="Guest List",
            description="List of all guests for the current event",
        ),
        3: dict(
            id=3,
            title="Daily Payments",
            description="Daily payments for the last 30 days",
        )
    }

    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description

    @staticmethod
    def all() -> list:
        return [ReportModel(**report) for report in list(ReportModel.reports.values())]

    @staticmethod
    def get(id: int) -> dict | None:
        if id in ReportModel.reports:
            return ReportModel(**ReportModel.reports[id])

        return None

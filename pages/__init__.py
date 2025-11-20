"""
Pages package for Depression Risk Assessment application.
"""

from pages.risk_assessment import render_risk_assessment_page
from pages.dashboard import render_dashboard_page
from pages.about import render_about_page

__all__ = [
    'render_risk_assessment_page',
    'render_dashboard_page',
    'render_about_page',
]

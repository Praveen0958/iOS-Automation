from behave import *
from pages.skiponboardingpage import skiponboarding

@Given('I click on Get Started button')
def verify_getstarted(context):
    onboarding_page = skiponboarding(context.driver)  # Create instance
    onboarding_page.init_elements()  # Initialize elements
    onboarding_page.tap_getstarted()  # Call method on the instance
    # Store the instance in the context for later use:
    context.onboarding_page = onboarding_page

@Then('I should navigate to Topics page and click do it later')
def verify_doitlater(context):
    context.onboarding_page.doitlaterlink() # Access stored instance

@Then('I should be routed to set up notifications and click on set up')
def verify_setupnotifs(context):
    context.onboarding_page.setup_notification()

@Then('I should be routed to set up tracking and click on set up')
def verify_setuptracking(context):
    context.onboarding_page.setup_tracking()

@Then('I should be routed to Home page and see Today logo')
def verify_homepagelanding(context):
    context.onboarding_page.home_page()


Feature: Skip Onboarding feature



Scenario: Verification of skip onboarding flow
 Given   I click on Get Started button
 Then    I should navigate to Topics page and click do it later
 Then    I should be routed to set up notifications and click on set up
 Then    I should be routed to set up tracking and click on set up
 Then    I should be routed to Home page and see Today logo  
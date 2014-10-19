Feature: Tools / Image collection
    Scenario: Links from home page
        Given opening browser with home page
        When all link are works and present texts
        And comeback to the home page
        Then open the "Tell us" pop up
        And fill all fields click button send

    Scenario: Check incoming message to admin
        Given login as admin
        And go to the drucode settings
        When you are on contact message tab
        Then find the user,mail,budget,message
        And all steps are passed
Feature: smart_watch search
    Scenario: smart_watch search
        Given User create driver
        And   User open url
        When  User close login window
        And   User search item 'smart watches'
        Then  User gets name and prices of the items
        Then  User close driver

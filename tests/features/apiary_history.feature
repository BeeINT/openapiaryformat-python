Feature: Testing History Apiary Features

   Scenario: Basic history size Test without activating
       Given I have a new Apiary
       Then I see the history is of size 0
       When I set the name to "My New Name"
       Then I see the history is of size 0

   Scenario: Basic history size Test with activating
       Given I have a new Apiary
       Then I see the history is of size 0
       Then I activate the history
       When I set the name to "My New Name"
       Then I see the history is of size 1
       Then I deactivate the history
       When I set the name to "My Newer Name"
       Then I see the history is of size 1
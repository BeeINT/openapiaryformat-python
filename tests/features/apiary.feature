Feature: Testing Basic Apiary Features


   Scenario: Create new Apiary with name and change it
       Given I have a new Apiary with the name "My Apiary"
       Then I see the name is "My Apiary"
       When I set the name to "My New Name"
       Then I see the name is "My New Name"

   Scenario: Create new Apiary and set the Name
       Given I have a new Apiary
       When I set the name to "My First Test"
       Then I see the name is "My First Test"

   Scenario: Name default is False
       Given I have a new Apiary
       Then I see the name is False

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
       
    Scenario: Test the Apiary default name
       Given I have a new Apiary with the name "My Apiary"
       Then the default representation of the apiary object is "My Apiary"

    Scenario: Test the Apiary dumps() returns a string of a minimal apiary
       Given I have a new Apiary with the name "My Apiary"
       Then dumps() should return a string of 51 characters
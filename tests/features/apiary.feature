Feature: Set name of an Apiary
   This is a test


   Scenario: Create new Apiary with name
       Given I have a new Apiary with the name "My Apiary"
       Then I see the name "My Apiary"
       When I set the name to "My New Name"
       Then I see the name "My New Name"

   Scenario: Set a Name
       Given I have a new Apiary
       When I set the name to "My First Test"
       Then I see the name "My First Test"
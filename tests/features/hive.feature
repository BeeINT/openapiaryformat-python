Feature: Testing Basic Hive Features


   Scenario: Create new Hive with name and change it
       Given I have a new Hive with the name "My Hive"
       Then I see the name is "My Hive"
       When I set the name to "My New Name"
       Then I see the name is "My New Name"

   Scenario: Create new Hive and set a name
       Given I have a new Hive
       Then I see the name is False
       When I set the name to "My New Name"
       Then I see the name is "My New Name"


    Scenario: Test the Hives default name
       Given I have a new Hive with the name "My Hive"
       Then the default representation of the apiary object is "My Hive"

    Scenario: Test the Hive dumps() returns a string of a minimal hive
       Given I have a new Hive with the name "My Hive"
       Then dumps() should return a string of 47 characters
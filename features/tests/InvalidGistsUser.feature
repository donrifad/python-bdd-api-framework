# Created by mohamedrifad at 7/4/22
Feature: Verify Gists Api With Invalid Users
  # Invalid token is provided for all tests

  @smoke @negative
  Scenario Outline: Add A Gists With Invalid User
    Given I have invalid github auth credentials
    And  I have the details with <description> and <filename> and <public> and <content>
    When I execute the CREATE gists api
    Then  I see the status code of 401
    Examples:
      | description         | filename  | public | content     |
      | Example of my gist2 | ReadMe.MD | false  | hello world |

  @smoke @negative
  Scenario: Get A Gists Using ID With Invalid User
    Given I have invalid github auth credentials
    When I execute the GET gists api with Gists ID 2a63dbfa9515944fdb2f01849303dd93
    Then  I see the status code of 401


   @smoke @negative
  Scenario Outline: Update A Gists Using ID
    Given I have invalid github auth credentials
    And I have the gists update details with gistsID  <description> and <filename> and <public> and <content> and <gists_id>
    Examples:
      | description         | filename  | public | content     |gists_id|
      | Example of my gist2 | ReadMe.MD | false  | hello world |2a63dbfa9515944fdb2f01849303dd93|
    When I execute the UPDATE gists api with Gists ID 2a63dbfa9515944fdb2f01849303dd93
    Then  I see the status code of 404


  @smoke @negative
  Scenario: Get the Lists of Gists Using UserID
    Given I have invalid github auth credentials
    When I execute the GETLIST api with donrifadswer
    Then  I see the status code of 404
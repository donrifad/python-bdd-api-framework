# Created by mohamedrifad at 7/3/22
Feature: Basic Api Functions ADD GET UPDATE DELETE
  # You should have a valid gist id

  @smoke @add
  Scenario Outline: Add A Gists
    Given I have github auth credentials
    And  I have the details with <description> and <filename> and <public> and <content>
    When I execute the CREATE gists api
    Then  I see the status code of 201
    And Gists is successfully added with <description> and <filename> and <public> and <content>
    Examples:
      | description         | filename  | public | content     |
      | Example of my gist2 | ReadMe.MD | false  | hello world |


  @smoke
  Scenario: Get A Gists Using ID
    Given I have github auth credentials
    When I execute the GET gists api with Gists ID 2a63dbfa9515944fdb2f01849303dd93
    Then  I see the status code of 200
    And I see the requested Gists ID 2a63dbfa9515944fdb2f01849303dd93

  @smoke
  Scenario Outline: Update A Gists Using ID
    Given I have github auth credentials
    And I have the gists update details with gistsID  <description> and <filename> and <public> and <content> and <gists_id>
    Examples:
      | description         | filename  | public | content     |gists_id|
      | Example of my gist2 | ReadMe.MD | false  | hello world |2a63dbfa9515944fdb2f01849303dd93|
    When I execute the UPDATE gists api with Gists ID 2a63dbfa9515944fdb2f01849303dd93
    Then  I see the status code of 200


  @smoke
  Scenario Outline: Get the Lists of Gists Using UserID
    Given I have github auth credentials
    When I execute the GETLIST api with donrifad
    Then  I see the status code of 200
    Then I see the following Gist IDS <ID_List>
    Examples:
      | ID_List                              |
      |efcd61a52f267ff414fe0b24e1504a8b,2a63dbfa9515944fdb2f01849303dd93,3cd891f2e67b5b984cd9c6ed09c8d49c|








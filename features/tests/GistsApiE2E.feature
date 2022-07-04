# Created by mohamedrifad at 7/3/22
Feature: Verify Basic Api Functions [Add,Edit,Delete] of Gists
  # Adding new gists
  # Update  the added gists
  # Then delete the added gists and verify the e2e flow

  @regression
  Scenario Outline: Verify adding updating deleting a gists
    Given I have github auth credentials
    And  I have the details with <description> and <filename> and <public> and <content>
    When I execute the CREATE gists api
    Then  I see the status code of 201
    And Gists is successfully added with <description> and <filename> and <public> and <content>
    Examples:
      | description         | filename  | public | content     |
      | Example of my gist2 | ReadMe.MD | false  | hello world |
    Given  I have the update details with <description> and <filename> and <public> and <content>
    When I execute the UPDATE gists Api
    Then  I see the status code of 200
    When I execute the Delete gists Api
    Then  I see the status code of 204
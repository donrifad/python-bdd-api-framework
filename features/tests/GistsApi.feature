# Created by mohamedrifad at 7/3/22
Feature: Verify basic Api Functions [Add,Edit,Delete] of Gists
  # Enter feature description here

  @regression
  Scenario Outline: Verify adding a gists
    Given I have github auth credentials
    And  I have the details with <description> and <filename> and <public> and <content>
    When I execute the create gists api
    Then  I see the status code of 201
    And Gists is successfully added with <description> and <filename> and <public> and <content>
    Examples:
      | description         | filename  | public | content     |
      | Example of my gist2 | ReadMe.MD | false  | hello world |
Feature: Weather Shop
  As a user
  I want to make a purchase from the weather app based on temperature
  So that I can get the right product for the given temperature

  Scenario: Purchase sunscreens for high temperature and moisturisers for low temperature
    Given User navigates to "https://weathershopper.pythonanywhere.com/"
    When User reads temperature and purchases products mentioned in "products.json"
    And User navigates to Cart
    And User pays with card using payment information from "payment.json"
    Then Verify that user is able to make payment successfully


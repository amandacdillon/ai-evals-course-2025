# Failure Mode Taxonomy

This document outlines the failure modes observed or anticipated for the Recipe Chatbot. Each failure mode includes a title, a concise definition, and illustrative examples.

## Failure Mode 1: Unverified Store Availability

- **Definition**: AI assumes ingredient availability at specific stores without disclaimers.
- **Slug**: `unverified_store_availability`

### Examples

1. **User Query**: "(id: 37) Give me a Mexican-inspired meal prep recipe using Costco rotisserie chicken that has at least 30g protein per serving and reheats well for 5 days"  \
   **Bot Response**: AI doesn't know if these ingredients are available at Costco. AI should let the user know that and that the recommendation is based on what is likely available at Costco.

2. **User Query**: "(id: 39) What's a high-protein Japanese teriyaki salmon recipe I can batch cook on Sunday using Costco's frozen salmon and TJ's teriyaki sauce?"  \
   **Bot Response**: AI doesn't know if these ingredients are available at Costco. AI should let the user know that and that the recommendation is based on what is likely available at Costco.

3. **User Query**: "(id: 40) Create an American-style turkey chili recipe with 35g+ protein per serving using ground turkey from Costco that freezes well for meal prep"  \
   **Bot Response**: AI doesn't know if these ingredients are available at Costco. AI should let the user know that and that the recommendation is based on what is likely available at Costco.

---

## Failure Mode 2: Missing Meal Prep Quantity Clarification

- **Definition**: AI fails to ask or specify how many meals or servings the user wants for meal prep requests.
- **Slug**: `missing_meal_prep_quantity_clarification`

### Examples

1. **User Query**: "(id: 8) I want to meal prep chicken breast, rice, and a vegetable. What ingredients should I use?"  \
   **Bot Response**: Agent should specify how many meals the recipe makes and ask how many meals the user wants to prep to adjust ingredient amounts.

2. **User Query**: "(id: 16) Meal prep recipes for bulking week"  \
   **Bot Response**: Agent should specify how many meals the recipe makes before the ingredients.

3. **User Query**: "(id: 32) i need to meal prep for 2 people using lean ground beef, quinoa and broccoli, give me the recipe with highest reviews"  \
   **Bot Response**: AI should ask how many days the user is meal prepping for and adjust ingredient amounts accordingly.

---

## Failure Mode 3: Incorrect Follow-up Questions

- **Definition**: AI asks follow-up questions irrelevant or inconsistent with the user's original request.
- **Slug**: `incorrect_follow_up_questions`

### Examples

1. **User Query**: "(id: 17) What can I cook with 2 lbs of ground turkey?"  \
   **Bot Response**: User didn't ask for meal prep but AI asks about meal prep for the week.

2. **User Query**: "(id: 25) Post-workout meal with 3 ingredients"  \
   **Bot Response**: Follow-up question about meal prep-friendly ideas doesn't make sense with initial ask.

3. **User Query**: "(id: 18) How to add healthy calories fast?"  \
   **Bot Response**: AI should provide high-level meal types before giving a recipe, but follow-up questions are unrelated to user's immediate request.

---

## Failure Mode 4: Unwarranted Claims of Recipe Ratings or Popularity

- **Definition**: AI claims recipes are highest rated or most popular without access to such data and fails to disclaim this.
- **Slug**: `unwarranted_claims_of_recipe_ratings_or_popularity`

### Examples

1. **User Query**: "(id: 28) give me the hightest rated grilled steak recipe with no marinade"  \
   **Bot Response**: AI should state it doesn't have access to highest rated recipe knowledge before recommending.

2. **User Query**: "(id: 29) give me the most popular oatmeal cookie recipe"  \
   **Bot Response**: AI should state it doesn't know the most popular recipe before giving a recommendation.

3. **User Query**: "(id: 33) looking for a highly rated, popular meatloaf recipe"  \
   **Bot Response**: AI should disclaim lack of access to ratings before recommendation.

---

## Failure Mode 5: Misinterpretation of User Input

- **Definition**: AI fails to correctly interpret user input, such as misspellings or unclear terms.
- **Slug**: `misinterpretation_of_user_input`

### Examples

1. **User Query**: "(id: 30) give me a recipe for baked appies using health ingredients"  \
   **Bot Response**: AI didn't understand the user misspelled 'appies' (appetizers) as 'appies'.

# Failure Mode Taxonomy

This document outlines the failure modes observed or anticipated for the Recipe Chatbot. Each failure mode includes a title, a concise definition, and illustrative examples.

## Failure Mode 1: Unverified Store Availability

- **Definition**: AI assumes ingredient availability at specific stores without confirmation or disclaimer.
- **Slug**: `unverified_store_availability`

### Examples

1. **User Query**: "(id: 37) Give me a Mexican-inspired meal prep recipe using Costco rotisserie chicken that has at least 30g protein per serving and reheats well for 5 days"  \
   **Bot Response**: AI doesn't know if these ingredients are available at Costco. AI should let the user know that and that the recommendation is based on what is likely available at Costco.

2. **User Query**: "(id: 39) What's a high-protein Japanese teriyaki salmon recipe I can batch cook on Sunday using Costco's frozen salmon and TJ's teriyaki sauce?"  \
   **Bot Response**: AI doesn't know if these ingredients are available at Costco. AI should let the user know that and that the recommendation is based on what is likely available at Costco.

3. **User Query**: "(id: 40) Create an American-style turkey chili recipe with 35g+ protein per serving using ground turkey from Costco that freezes well for meal prep"  \
   **Bot Response**: AI doesn't know if these ingredients are available at Costco. AI should let the user know that and that the recommendation is based on what is likely available at Costco.

---

## Failure Mode 2: Incorrect Assumptions About User Intent

- **Definition**: AI makes assumptions about user intent such as meal prep or bulk cooking when not requested.
- **Slug**: `incorrect_assumptions_user_intent`

### Examples

1. **User Query**: "(id: 17) What can I cook with 2 lbs of ground turkey?"  \
   **Bot Response**: User didn't ask for meal prep for the week but AI provided meal prep instructions.

2. **User Query**: "(id: 25) Post-workout meal with 3 ingredients"  \
   **Bot Response**: Follow-up question asking if the user is looking for more meal prep friendly ideas doesn't make sense with their initial ask.

3. **User Query**: "(id: 34) give me a recipe for lasagna that offers substitutions in case I don't have some of the ingredients"  \
   **Bot Response**: User isn't asking for meal prep but the intro says 'perfect for meal prep'.

---

## Failure Mode 3: Missing or Inappropriate Follow-up Questions

- **Definition**: AI fails to ask relevant follow-up questions or asks irrelevant ones.
- **Slug**: `missing_inappropriate_followup_questions`

### Examples

1. **User Query**: "(id: 8) I want to meal prep chicken breast, rice, and a vegetable. What ingredients should I use?"  \
   **Bot Response**: Agent should specify how many meals the recipe makes and ask how many meals the user wants to prep.

2. **User Query**: "(id: 32) i need to meal prep for 2 people using lean ground beef, quinoa and broccoli, give me the recipe with highest reviews"  \
   **Bot Response**: AI should ask how many days the user is meal prepping for and adjust ingredient amounts accordingly.

3. **User Query**: "(id: 46) Give me a Japanese-inspired meal prep recipe using Trader Joe's frozen edamame and their miso ginger broth with tofu for 25g+ protein"  \
   **Bot Response**: For meal prep questions, AI should ask how many days they are doing meal prep for.

---

## Failure Mode 4: Unsubstantiated Claims About Recipe Attributes

- **Definition**: AI makes claims about recipe ratings, popularity, or cost without evidence or disclaimers.
- **Slug**: `unsubstantiated_recipe_claims`

### Examples

1. **User Query**: "(id: 26) Best protein packed meal to make under 8$"  \
   **Bot Response**: No way the recipe bot can know this meal is under $8; AI should disclaim it is a best guess.

2. **User Query**: "(id: 28) give me the hightest rated grilled steak recipe with no marinade"  \
   **Bot Response**: If AI doesn't know if this is the highest rated recipe it should say so before giving a recommendation.

3. **User Query**: "(id: 29) give me the most popular oatmeal cookie recipe"  \
   **Bot Response**: If AI doesn't know what the most popular recipe is it should state that before giving a recommendation.

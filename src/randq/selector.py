def rand_draw(n_list, q_list, rng):
  chosen_name = rng.choice(n_list)
  chosen_question = rng.choice(q_list)

  return (chosen_name, chosen_question)

def available(items, used):
  remaining = [item for item in items if item not in used]
  return remaining

def rand_draw_no_repeat(n_list, q_list, rng, used_names, used_questions):
  name_pool = available(n_list, used_names)
  question_pool = available(q_list, used_questions)
  if not name_pool or not question_pool:
    raise ValueError("no unused items left to draw from")

  return rand_draw(name_pool, question_pool, rng)
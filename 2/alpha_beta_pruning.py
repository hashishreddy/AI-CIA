def game_solver(depth, pos, is_player_turn, outcomes, low, high):
    if depth == 3:  
        return outcomes[pos]

    if is_player_turn:
        max_outcome = float('-inf')
        for option in range(2):
            value = game_solver(depth + 1, pos * 2 + option, False, outcomes, low, high)
            max_outcome = max(max_outcome, value)
            low = max(low, value)
            if low >= high:
                break
        return max_outcome
    else:
        min_outcome = float('inf')
        for option in range(2):
            value = game_solver(depth + 1, pos * 2 + option, True, outcomes, low, high)
            min_outcome = min(min_outcome, value)
            high = min(high, value)
            if low >= high:
                break
        return min_outcome


if __name__ == "__main__":

    final_scores = [3, -8, 2, -5, 9, -4, 7, -1]

    alpha_init = float('-inf')
    beta_init = float('inf')

    result = game_solver(0, 0, True, final_scores, alpha_init, beta_init)
    print(f"result : {result}")

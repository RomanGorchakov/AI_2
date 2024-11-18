#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import deque

def PourProblem(initial, target, sizes):
    def Fill(state, i):
        new_state = list(state)
        new_state[i] = sizes[i]
        return tuple(new_state)

    def Dump(state, i):
        new_state = list(state)
        new_state[i] = 0
        return tuple(new_state)

    def Pour(state, i, j):
        new_state = list(state)
        Pour_amount = min(state[i], sizes[j] - state[j])
        new_state[i] -= Pour_amount
        new_state[j] += Pour_amount
        return tuple(new_state)

    initial_state = tuple(initial)
    queue = deque([(initial_state, [], [initial_state])])  # Добавляем начальное состояние в очередь
    visited = {initial_state}

    while queue:
        current_state, path, states_history = queue.popleft()

        if target in current_state:
            return path, current_state, states_history  # Возвращаем историю состояний

        for i in range(len(sizes)):
            new_state = Fill(current_state, i)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [('Fill', i)], states_history + [new_state]))

            new_state = Dump(current_state, i)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [('Dump', i)], states_history + [new_state]))

            for j in range(len(sizes)):
                if i != j:
                    new_state = Pour(current_state, i, j)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [('Pour', i, j)], states_history + [new_state]))

    return None

if __name__ == "__main__":
    initial_state = (1, 1, 1)
    target_volume = 13
    sizes = (2, 16, 32)
    result = PourProblem(initial_state, target_volume, sizes)

    if result:
        path, final_state, states_history = result
        print(path, states_history)
    else:
        print("У этой задачи нет решения.")
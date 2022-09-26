# """
# 역전 카운트로 이동 가능성 판단
# nxn 보드에서 빈칸이 아닌 숫자들을 일렬로 나열 했을 때
# n이 홀수인 경우, 역전 카운트가 짝수면 이동가능
# n이 짝수인 경우, 빈칸의 행 위치가 아래서부터 짝수인 행에 있으면 역전 카운트가 홀수 일 때 이동 가능
#              빈칸의 행 위치가 아래서부터 홀수인 행에 있으면 역전 카운트가 짝수일 때 이동 가능
#
# 맨하탄 거리
# 시간 복잡도도 물론 줄여야 하지만 공간 복잡도 또한 줄여야함
# """
#
from queue import PriorityQueue


class AStar:
    def __init__(self, problem, answer, moves=0):
        self.problem = problem
        self.answer = answer
        self.moves = moves

    def __lt__(self, other):
        return self.f() < other.f()

    def f(self):
        "비용"
        return self.g() + self.h()

    def g(self):
        "시작점"
        return self.moves

    def h(self):
        """Manhattan heuristics 추정비용"""
        dist = 0
        size = 3
        for i in range(9):
            goal_id = self.answer[i]
            # print(f'goal_id:{goal_id} {self.problem} {self.answer}')
            g_x = i // size
            g_y = i % 3
            # 2를 3으로 나누었을때 몫이 2가 나와야 하는데 왜 1이 나오냐 이기
            p_x = self.problem.index(goal_id) // size # 0이 나와야 하는데 왜 1이 나옴?
            p_y = self.problem.index(goal_id) % 3
            dist += abs(p_x - g_x) + abs(p_y - g_y)
            # print(g_x, g_y)
            # print(p_x, p_y)
        return dist


def generate_child(node: AStar, current, target):  # node 이동시키기
    copy_board = node.problem[:]
    # print(current, target, copy_board[current], copy_board[target])
    copy_board[current], copy_board[target] = copy_board[target], copy_board[current]
    # print(copy_board)
    return AStar(copy_board, node.answer, node.moves+1)


def expand_child(node: AStar):  # node가 어떤 방향으로 이동할 수 있는지 확인하고 result에 담기
    result = []
    pos = node.problem.index(0)  # 빈칸의 위치
    # print(node.problem, pos)
    if not pos in (0, 1, 2):  # UP
        result.append(generate_child(node, pos, pos - 3))
    if not pos in (0, 3, 6):  # LEFT
        result.append(generate_child(node, pos, pos - 1))
    if not pos in (2, 5, 8):  # RIGHT
        result.append(generate_child(node, pos, pos + 1))
    if not pos in (6, 7, 8):  # DOWN
        result.append(generate_child(node, pos, pos + 3))
    # for i in result:
    #     print(i.problem)
    return result


"""
     첨 시작할때 start node 넣고 돌림
     open_list랑 answer랑 같은지 확인하고 같으면 그대로 끝내고
     같지 않으면 현재 노드를 closed_list에 넣고
     그 다음 자식 노드들 생성하고 open_list에 넣고
     하나를 curent_node에 넣기
"""

def list_to_str(l):
    r = ""
    for n in l:
        r += str(n)
    return r

def problem_solver(node: AStar):
    """
        open_list는 생성된 child node를 넣고
        이 node에 대한 child node를 생성해서 또 open_list에 넣는다
        탐색 성공이 출력되게 하는 것
    """

    open_queue = PriorityQueue() # 선입선출 + 우선순위
    open_queue.put(node)  # h, problem에 대한 pq
    open_set = set()
    open_set.add(list_to_str(node.problem))
    closed_set = set()
    solve_path = []

    while_cnt = 0
    while not open_queue.empty():
    # for _ in range(6):
        while_cnt += 1

        print(f'while_cnt:{while_cnt} open_set_cnt:{len(open_set)} open_queue_cnt:{open_queue.qsize()}', )

        current_list = open_queue.get()
        print('current_list:', current_list.problem)
        # print(current_list.problem)
        if current_list.problem == node.answer:
            print("탐색 성공")
            break
        # print(current_list.problem, open_set)
        open_set.remove(list_to_str(current_list.problem))
        closed_set.add(list_to_str(current_list.problem))
        for state in expand_child(current_list):    # ()안에 노드 여야함
            print(f'problem:{state.problem}, f:{state.f()} h:{state.h()}  closed_list_cnt:{len(closed_set)}')
            # open_set에도 없고 closed_set에도 없으면 open_set과 open_queue에 넣어라
            # 왜냐하면 방문한 적이 없기 때문이다 closed_set에 없으면 방문한 적이 없는거니까
            if list_to_str(state.problem) not in open_set and list_to_str(state.problem) not in closed_set:  # open_set에 없으면 새로운거니까 추가
                # print(state.problem, open_se)

                # 중복 check
                open_set.add(list_to_str(state.problem)) # 여기에서 중복이 발생 할 수 있다.
                open_queue.put(state)
            if list_to_str(state.problem) in closed_set :  # close set에 있으면 넘어가기
                print(f'중복 노선 while_cnt:{while_cnt}', state.problem, open_set)
                continue
    return solve_path


def print_path(start, goal, past):
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = past[node]
    path.append(start)
    for each in path[::-1]:
        print(''.join(each[:3]))
        print(''.join(each[3:6]))
        print(''.join(each[6:]))
        print('-------------')


if __name__ == "__main__":
    puzzle = [2, 8, 3, 1, 6, 4, 7, 0 ,5]
    # goal = [2, 8, 3, 1, 6, 4, 7, 5 ,0]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    start = AStar(problem=puzzle, answer=goal)
    # marked = fuck(start)
    # print(marked)
    print(problem_solver(start))
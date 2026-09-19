import sys
from collections import deque


def main():
    rd = sys.stdin.buffer.readline

    first = rd().split()
    if not first:
        return

    K = int(first[0])
    num_layers = int(first[5])

    second = rd().split()
    if not second:
        return

    N_line = rd()
    if not N_line:
        return

    N = int(N_line)

    for _ in range(N):
        if not rd():
            return

    MAXR = 2005

    NOT_ARRIVED = 0
    READY_P_PRE = 1
    WAIT_P_UP = 2
    READY_P_PROC = 3
    WAIT_P_DOWN = 4
    READY_P_POST = 5
    WAIT_P_POST = 6
    READY_D_PRE = 7
    WAIT_D_UP = 8
    READY_D_PROC = 9
    WAIT_D_DOWN = 10
    READY_D_POST = 11
    WAIT_D_POST = 12
    FINISHED = 13

    state = [NOT_ARRIVED] * MAXR
    remote = [-1] * MAXR

    remote_load = [0] * K

    edge_free = True
    cloud_free = [True] * K

    q_p_pre = deque()
    q_p_post = deque()

    q_p_proc = [deque() for _ in range(K)]

    ready_d_pre = set()
    ready_d_post = set()
    ready_d_proc = [set() for _ in range(K)]

    def pop_queue(q, wanted):
        while q:
            rid = q.popleft()
            if state[rid] == wanted:
                return rid
        return -1

    while True:
        line = rd()

        if not line:
            return

        line = line.strip()

        if not line:
            continue

        if line == b"END":
            return

        count_line = rd()

        if not count_line:
            return

        e = int(count_line)

        events = []
        frame_finished = set()

        for _ in range(e):
            parts = rd().split()

            if not parts:
                return

            events.append(parts)

            if parts[0] == b"FIN":
                frame_finished.add(int(parts[1]))

        for parts in events:
            typ = parts[0]

            if typ == b"ARR":
                rid = int(parts[1])

                state[rid] = READY_P_PRE
                q_p_pre.append(rid)

            elif typ == b"TDN":
                server = parts[1]

                if server == b"E":
                    edge_free = True
                else:
                    k = int(server[1:])
                    cloud_free[k] = True

                phase = parts[2]
                step = parts[3]

                if phase == b"P" and step == b"POST":
                    rid = int(parts[5])

                    if rid not in frame_finished:
                        state[rid] = READY_D_PRE
                        ready_d_pre.add(rid)

                elif phase == b"D" and step == b"POST":
                    m = int(parts[5])

                    for j in range(m):
                        rid = int(parts[6 + j])

                        if rid not in frame_finished:
                            state[rid] = READY_D_PRE
                            ready_d_pre.add(rid)

            elif typ == b"XDN":
                direction = parts[1]
                k = int(parts[2])
                kind = parts[4]
                m = int(parts[5])

                ids = []

                for j in range(m):
                    ids.append(int(parts[6 + j]))

                if kind == b"PRE":
                    rid = ids[0]

                    if direction == b"UP":
                        state[rid] = READY_P_PROC
                        q_p_proc[k].append(rid)

                    else:
                        state[rid] = READY_P_POST
                        q_p_post.append(rid)

                else:
                    if direction == b"UP":
                        for rid in ids:
                            state[rid] = READY_D_PROC
                            ready_d_proc[k].add(rid)

                    else:
                        for rid in ids:
                            state[rid] = READY_D_POST
                            ready_d_post.add(rid)

        for rid in frame_finished:
            k = remote[rid]

            if k >= 0 and remote_load[k] > 0:
                remote_load[k] -= 1

            state[rid] = FINISHED

            ready_d_pre.discard(rid)
            ready_d_post.discard(rid)

            if k >= 0:
                ready_d_proc[k].discard(rid)

        answer = []

        if edge_free:
            if ready_d_post:
                ids = []

                for rid in ready_d_post:
                    if state[rid] == READY_D_POST:
                        ids.append(rid)

                ready_d_post.clear()

                if ids:
                    for rid in ids:
                        state[rid] = WAIT_D_POST

                    answer.append(
                        "E D POST -1 {} {}".format(len(ids), " ".join(map(str, ids)))
                    )

                    edge_free = False

        if edge_free:
            rid = pop_queue(q_p_post, READY_P_POST)

            if rid != -1:
                answer.append(f"E P POST {remote[rid]} {rid}")

                state[rid] = WAIT_P_POST
                edge_free = False

        if edge_free:
            if ready_d_pre:
                ids = []

                for rid in ready_d_pre:
                    if state[rid] == READY_D_PRE:
                        ids.append(rid)

                ready_d_pre.clear()

                if ids:
                    for rid in ids:
                        state[rid] = WAIT_D_UP

                    answer.append(
                        "E D PRE -1 {} {}".format(len(ids), " ".join(map(str, ids)))
                    )

                    edge_free = False

        if edge_free:
            rid = pop_queue(q_p_pre, READY_P_PRE)

            if rid != -1:
                best_remote = 0

                for k in range(1, K):
                    if remote_load[k] < remote_load[best_remote]:
                        best_remote = k

                remote[rid] = best_remote
                remote_load[best_remote] += 1

                state[rid] = WAIT_P_UP

                answer.append(f"E P PRE {best_remote} {rid}")

                edge_free = False

        for k in range(K):
            if not cloud_free[k]:
                continue

            if ready_d_proc[k]:
                ids = []

                for rid in ready_d_proc[k]:
                    if state[rid] == READY_D_PROC:
                        ids.append(rid)

                ready_d_proc[k].clear()

                if ids:
                    for rid in ids:
                        state[rid] = WAIT_D_DOWN

                    answer.append(
                        "C{} D PROC {} {} {}".format(
                            k, k, len(ids), " ".join(map(str, ids))
                        )
                    )

                    cloud_free[k] = False

            if cloud_free[k]:
                rid = pop_queue(q_p_proc[k], READY_P_PROC)

                if rid != -1:
                    state[rid] = WAIT_P_DOWN

                    answer.append(f"C{k} P PROC 0 {num_layers} {k} {rid}")

                    cloud_free[k] = False

        sys.stdout.write(str(len(answer)) + "\n")

        if answer:
            sys.stdout.write("\n".join(answer) + "\n")

        sys.stdout.flush()


if __name__ == "__main__":
    main()

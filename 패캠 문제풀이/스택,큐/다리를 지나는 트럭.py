#문제풀이:
#   answer는 초를 세주는 걸로 반목마다 1씩 증가.
#   bridge_on은 다리의 길이만큼 리스트를 만듬(트럭이 시간에 따라 지날 때마다 반영 해줄 수 있기 때문) ex) 다리길이가 3 -> [0,0,0]
#   curr_weight는 현재 다리에 올라와 있는 무게.(초기 = 0)
#   truck_weights에 원소가 남아 있을때 까지 반복( 트럭이 모두 지나갈때 까지 반복)
#   반복할때마다 초를 1씩 증가해주고 1초가 지나갈때 마다 bridge_on 리스트 에 맨 앞 원소를 pop(0), 삭제된 원소의 무게를 현재 무게에서 빼준다.
#   1) 현재 무게 + truck_weigths[0] 가 다리의 길이보다 크다면
#       다리에 새로운 트럭이 올라오지 못하므로 0으로 append 시킨다.
#   2) 작다면
#       truck_weights 리스트에서 pop(0) 한후 bridge_on에 append 시킨다 ( 트럭이 다리위로 올라간다 )
#       새로 들어온 트럭 무게를 curr_weight(현재무게)에 더해줌
#   모든 트럭이 다리위로 올라갔다면 ( truck_weights 리스트는 빈 리스트가 되어 첫번째 while이 종료 된다)
#   curr_weight가 0이 될때 까지 반복 (다리위에 올라간 트럭이 모두 다 다리를 지나간 시간을 구해줘야한다)
#   answer(초)는 계속 1씩 증가하고
#   1초가 지나갈때마다 bridge_on에서 pop(0)을 하여 curr_weight에 빠진 원소를 빼준다.

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_on = [0] * bridge_length
    curr_weight = 0

    while truck_weights:
        answer += 1
        bridge_out = bridge_on.pop(0)
        curr_weight -= bridge_out

        if curr_weight + truck_weights[0] > weight:
            bridge_on.append(0)
        else:
            truck = truck_weights.pop(0)
            bridge_on.append(truck)
            curr_weight += truck

    while curr_weight > 0:
        answer += 1
        bridge_out = bridge_on.pop(0)
        curr_weight -= bridge_out

    return answer

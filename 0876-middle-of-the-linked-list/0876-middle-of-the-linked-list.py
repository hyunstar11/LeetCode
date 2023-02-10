# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 워커와 러너를 선언 
        walker = head 
        runner = head
        
        # 러너가 끝 (null이나 마지막 노드에 도착할 때 링크드 노드가 끝난다? -> 이건 나중에 설명 다시 한 번 보기)
        while runner and runner.next:
            # 1 step
            # 워커가 한 스텝을 이동 
            walker = walker.next
            
            # 2 step
            # 러너는 두 스텝을 이동한다 
            runner = runner.next.next
        
        #워커 반환 
        return walker
        

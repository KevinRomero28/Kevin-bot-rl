from util.objects import *
from util.routines import *
from util.tools import find_hits 


class Bot(GoslingAgent):
    def run(self):
        if self.intent is not None:
           return
        ball_to_foe_goal_y=abs(self.ball.location.y-self.foe_goal.location.y)
        my_location_to_foe_location=abs(self.me.location.y-self.foe_goal.location.y)
        is_in_front_of_ball = ball_to_foe_goal_y > my_location_to_foe_location
        self_location_to_friend_goal_right_post=abs((self.me.location - self.friend_goal.right_post).magnitude())
        D4=(self.me.location.z-self.ball.location.z)
        # foe.location from me
        #foe.lopcation from the_ball 
        # friend.location_from_the_ball 

        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        
        if self_location_to_friend_goal_right_post > 1000:
            self.set_intent(goto(self.ball.location))
            targets ={'at_opponent_goal':(self.foe_goal.left_post, self.foe_goal_post), 
            'away_from_our_net':(self.friend_goal.right_post,self.friend_goal.left_post)}
            hits= find_hits(self, targets)

            return
        
        if is_in_front_of_ball or self.me.location :
            self.set_intent(goto(self.friend_goal.right_post,self.friend_goal.left_post))
            return 


        if self.me.boost > 80:
            self.set_intent(short_shot(self.foe_goal.location))
            return


            
        targets ={'at_opponent_goal':(self.foe_goal.left_post, self.foe_goal_post), 
         'away_from_our_net':(self.friend_goal.right_post,self.friend_goal.left_post)}
        hits= find_hits(self, targets)
    
        closest_boost = self.get_closest_large_boost()
        if closest_boost is not None:
            self.set_intent(goto(closest_boost.location))
            return
        self.set_intent(jump_shot)
        
            
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
        self_location_to_ball_location_z=(self.me.location.z-self.ball.location.z)
        #foe_location_from_me=
        #foe_location_from_the_ball= 
        friend_location_from_the_ball=self.me.location-self.ball.location 

        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        
        def run(self,agent):
            target= agent.ball.location + Vector3(0,200*side(agent.team),0)
            local_target = agent.me.local(target-agent.me.location)
            defaultPD(agent,local_target)
            defaultThrottle(agent,2300)
            if local_target.magnitude() < 650:
                agent.set_intent(
                    flip(agent.me.local(agent.foe_goal.location - agent.me.location)))
                if self.me.boost > 80:
                    self.set_intent(short_shot(self.foe_goal.location))
            return
                
        
        #if self_location_to_friend_goal_right_post > 1000:
            self.set_intent(goto(self.ball.location))
            targets ={'at_opponent_goal':(self.foe_goal.left_post, self.foe_goal_post), 
            'away_from_our_net':(self.friend_goal.right_post,self.friend_goal.left_post)}
            hits= find_hits(self, targets)

            if len(hits['at_opponent_goal']) > 0:
                self.set_intent(hits['at_opponent_goal'])
                
            
            if len(hits['away_from_our_net']) > 0:
                self.set_intent(hits['away_from_our_net'])
                

            return
        
        #if is_in_front_of_ball or self.me.location > my_location_to_foe_location:
            self.set_intent(hits)['at_opponent_goal'] > 0
                
    


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
        self.set_intent(short_shot(self.foe_goal.location))
        
            
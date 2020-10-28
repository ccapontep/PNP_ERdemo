(define (domain ER-domain)
    (:requirements :strips)
    (:predicates    (at ?x ?y) (adj ?x ?y) (rob ?x)
                    (busy ?x) (person ?x) (request ?x ?y ?z) (conv ?topic ?loc) 
                    (issue ?x) (movingTogether ?to) )

    (:action moveRobot
        :parameters (?robot ?from ?to)
        :precondition (and (at ?robot ?from)
        		       (adj ?from ?to)
                       (rob ?robot)
                       (not (busy ?to)))
                       
        :effect (and (not (at ?robot ?from)) 
                          (at ?robot ?to)))
                         

    ; accompany human -- Barcelona with provide action in actionlib format
    ; until then, use only move robot. Assume human is moving with robot. 
    ; until Barcelona merge
    (:action accompanyHuman
        :parameters (?robot ?human ?topic ?from ?to )
        :precondition (and  (at ?robot ?from)
            		        (adj ?from ?to)
            		      ;  (at ?human ?from)
                            (person ?human)
                            (rob ?robot)
                            (not (movingTogether ?to))
                            (not (busy ?to))
                            (request ?robot ?human ?topic))
                       
        :effect (and        (not (at ?robot ?from))
                            (at ?robot ?to)
                            (movingTogether ?to)
                            (request ?robot ?human ?topic)
                            ; (not (at ?human ?from))
                            ; (at ?human ?to))
                            ))

    ; dialog, which has speak and listen inside it
    ; use topic such as get-patient-data  
    (:action dialog
        :parameters (?robot ?topic ?human ?loc)
        :precondition (and (at ?robot ?loc)
                           (at ?human ?loc)
                           (rob ?robot)
                           (person ?human)
                           (conv ?topic ?loc)
                           (not (request ?robot ?human ?topic)))
        :effect (and (request ?robot ?human ?topic)))
 


    (:action resolveIssue
        :parameters (?problem ?robot ?topic ?human ?loc)
        :precondition (and (at ?robot ?loc)
                        ;   (at ?human ?loc)
                           (rob ?robot)
                           (person ?human)
                           (issue ?problem)
                           (request ?robot ?human ?topic)
                           )
        :effect (and (not (issue ?problem))))
    
    
)


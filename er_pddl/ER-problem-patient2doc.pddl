(define (problem ER-problem-patient2doc)
    (:domain ER-domain)
    (:objects   main-enterance
                main-admission
                main-corridor
                main-triage
                
                waiting-room
                bathrooms-patients
                bathrooms-staff
                staff-lounge
                storage-equipment
                admin-checkout
                
                ambulance-enterance
                ambulance-admission
                ambulance-triage
                ambulance-corridor
                
                consulting-room-1
                consulting-room-2
                consulting-room-3
                consulting-room-4
                consulting-corridor
                
                bed-1 bed-2 bed-3
                bed-4 bed-5 bed-6
                bed-7
                bed-corridor
                
                examination-xray
                operating-room
                operating-corridor
                
                
                robot
                human
                error2solve
                topic
                patient-data
                request-done
                patient-request
                water
                accompany
                appt-time
                done-patient2doc
                )

    (:init  (adj main-corridor main-admission) (adj main-admission main-corridor)
            (adj main-corridor admin-checkout) (adj admin-checkout main-corridor)
            (adj main-corridor main-triage) (adj main-triage main-corridor) 
            (adj main-corridor main-enterance) (adj main-enterance main-corridor) 
            (adj main-corridor waiting-room) (adj waiting-room main-corridor) 
            (adj main-corridor bathrooms-patients) (adj bathrooms-patients main-corridor)
            
            (adj waiting-room bathrooms-patients) (adj bathrooms-patients waiting-room)
            (adj bathrooms-staff staff-lounge) (adj staff-lounge bathrooms-staff)
            (adj main-admission admin-checkout) (adj admin-checkout main-admission)
            
            (adj main-corridor ambulance-corridor) (adj ambulance-corridor main-corridor)
            (adj ambulance-corridor consulting-corridor) (adj consulting-corridor ambulance-corridor)
            (adj consulting-corridor operating-corridor) (adj operating-corridor consulting-corridor)
            (adj operating-corridor bed-corridor) (adj bed-corridor operating-corridor)
            (adj bed-corridor ambulance-corridor) (adj ambulance-corridor bed-corridor)
            
            (adj ambulance-corridor ambulance-triage) (adj ambulance-triage ambulance-corridor)
            (adj ambulance-corridor storage-equipment) (adj storage-equipment ambulance-corridor)
            (adj ambulance-corridor ambulance-enterance) (adj ambulance-enterance ambulance-corridor)
            (adj ambulance-corridor ambulance-admission) (adj ambulance-admission ambulance-corridor)
            (adj ambulance-corridor bathrooms-staff) (adj bathrooms-staff ambulance-corridor)
            (adj ambulance-corridor staff-lounge) (adj staff-lounge ambulance-corridor)
            
            (adj consulting-corridor consulting-room-1) (adj consulting-room-1 consulting-corridor)
            (adj consulting-corridor consulting-room-2) (adj consulting-room-2 consulting-corridor)
            (adj consulting-corridor consulting-room-3) (adj consulting-room-3 consulting-corridor)
            (adj consulting-corridor consulting-room-4) (adj consulting-room-4 consulting-corridor)
            (adj consulting-corridor examination-xray) (adj examination-xray consulting-corridor)
            (adj consulting-corridor operating-room) (adj operating-room consulting-corridor)
            
            (adj operating-corridor examination-xray) (adj examination-xray operating-corridor)
            (adj operating-corridor operating-room) (adj operating-room operating-corridor)
            
            (adj examination-xray storage-equipment) (adj storage-equipment examination-xray)
            
            (adj bed-corridor bed-1) (adj bed-1 bed-corridor)
            (adj bed-corridor bed-2) (adj bed-2 bed-corridor)
            (adj bed-corridor bed-3) (adj bed-3 bed-corridor)
            (adj bed-corridor bed-4) (adj bed-4 bed-corridor)
            (adj bed-corridor bed-5) (adj bed-5 bed-corridor)
            (adj bed-corridor bed-6) (adj bed-6 bed-corridor)
            (adj bed-corridor bed-7) (adj bed-7 bed-corridor)
            (adj bed-corridor examination-xray) (adj examination-xray bed-corridor)
            (adj bed-corridor operating-room) (adj operating-room bed-corridor)
            
            (busy bed-2) (busy bed-6) (busy consulting-room-3) (busy bathrooms-patients)
            
            (at human waiting-room) 
            (person human)
            
            (at robot main-triage)
            (rob robot)
            
            (conv topic)
            (issue error2solve)

            (time4appt appt-time)
            
            (Pwater water)
            (at water storage-equipment)
            (return-robot main-triage)
            )

    (:goal (and (Pdata patient-data waiting-room)
                (move-with-human accompany consulting-room-1)
                ; (req-done accompany)
                ; (robot-home accompany)
                
                ; (at robot consulting-room-1)
                ; (at human consulting-room-1)
                )))
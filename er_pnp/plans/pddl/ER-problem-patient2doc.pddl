(define (problem ER-problem-patient2doc)
    (:domain ER-domain)
    (:objects   mainEnterance
                mainAdmission
                mainCorridor
                mainTriage
                
                waitingRoom
                bathroomsPatients
                bathroomsStaff
                staffLounge
                storageEquipment
                adminCheckout
                
                ambulanceEnterance
                ambulanceAdmission
                ambulanceTriage
                ambulanceCorridor
                
                consultingRoom1
                consultingRoom2
                consultingRoom3
                consultingRoom4
                
                consultingRoom1out
                consultingRoom2out
                consultingRoom3out
                consultingRoom4out
                
                consultingCorridor
                
                bed1 bed2 bed3
                bed4 bed5 bed6
                bed7
                bedCorridor
                
                examinationXray
                operatingRoom
                operatingCorridor
                
                
                robot
                human
                lostPerson
                getPatientData
                GoTogether
                ; requestDone
                ; patientRequest
                ; accompany
                )

    (:init  (adj mainCorridor mainAdmission) (adj mainAdmission mainCorridor)
            (adj mainCorridor adminCheckout) (adj adminCheckout mainCorridor)
            (adj mainCorridor mainTriage) (adj mainTriage mainCorridor) 
            (adj mainCorridor mainEnterance) (adj mainEnterance mainCorridor) 
            (adj mainCorridor waitingRoom) (adj waitingRoom mainCorridor) 
            (adj mainCorridor bathroomsPatients) (adj bathroomsPatients mainCorridor)
            
            (adj waitingRoom bathroomsPatients) (adj bathroomsPatients waitingRoom)
            (adj bathroomsStaff staffLounge) (adj staffLounge bathroomsStaff)
            (adj mainAdmission adminCheckout) (adj adminCheckout mainAdmission)
            
            (adj mainCorridor ambulanceCorridor) (adj ambulanceCorridor mainCorridor)
            (adj ambulanceCorridor consultingCorridor) (adj consultingCorridor ambulanceCorridor)
            (adj consultingCorridor operatingCorridor) (adj operatingCorridor consultingCorridor)
            (adj operatingCorridor bedCorridor) (adj bedCorridor operatingCorridor)
            (adj bedCorridor ambulanceCorridor) (adj ambulanceCorridor bedCorridor)
            
            (adj ambulanceCorridor ambulanceTriage) (adj ambulanceTriage ambulanceCorridor)
            (adj ambulanceCorridor storageEquipment) (adj storageEquipment ambulanceCorridor)
            (adj ambulanceCorridor ambulanceEnterance) (adj ambulanceEnterance ambulanceCorridor)
            (adj ambulanceCorridor ambulanceAdmission) (adj ambulanceAdmission ambulanceCorridor)
            (adj ambulanceCorridor bathroomsStaff) (adj bathroomsStaff ambulanceCorridor)
            (adj ambulanceCorridor staffLounge) (adj staffLounge ambulanceCorridor)
            
            (adj consultingCorridor consultingRoom1out) (adj consultingRoom1out consultingCorridor)
            (adj consultingCorridor consultingRoom2out) (adj consultingRoom2out consultingCorridor)
            (adj consultingCorridor consultingRoom3out) (adj consultingRoom3out consultingCorridor)
            (adj consultingCorridor consultingRoom4out) (adj consultingRoom4out consultingCorridor)
            
            (adj consultingRoom1out consultingRoom1) (adj consultingRoom1 consultingRoom1out)
            (adj consultingRoom2out consultingRoom2) (adj consultingRoom2 consultingRoom2out)
            (adj consultingRoom3out consultingRoom3) (adj consultingRoom3 consultingRoom3out)
            (adj consultingRoom4out consultingRoom4) (adj consultingRoom4 consultingRoom4out)
            
            (adj consultingCorridor examinationXray) (adj examinationXray consultingCorridor)
            (adj consultingCorridor operatingRoom) (adj operatingRoom consultingCorridor)
            
            (adj operatingCorridor examinationXray) (adj examinationXray operatingCorridor)
            (adj operatingCorridor operatingRoom) (adj operatingRoom operatingCorridor)
            
            (adj examinationXray storageEquipment) (adj storageEquipment examinationXray)
            
            (adj bedCorridor bed1) (adj bed1 bedCorridor)
            (adj bedCorridor bed2) (adj bed2 bedCorridor)
            (adj bedCorridor bed3) (adj bed3 bedCorridor)
            (adj bedCorridor bed4) (adj bed4 bedCorridor)
            (adj bedCorridor bed5) (adj bed5 bedCorridor)
            (adj bedCorridor bed6) (adj bed6 bedCorridor)
            (adj bedCorridor bed7) (adj bed7 bedCorridor)
            (adj bedCorridor examinationXray) (adj examinationXray bedCorridor)
            (adj bedCorridor operatingRoom) (adj operatingRoom bedCorridor)
            
            (busy bed2) (busy bed6) (busy consultingRoom3) (busy bathroomsPatients)
            
            (at human waitingRoom) 
            (person human)
            
            (at robot mainTriage)
            (rob robot)
            
            (issue lostPerson)
            (conv getPatientData waitingRoom)
            
            )

    (:goal (and 
                (request robot human getPatientData)
                (movingTogether consultingRoom1)
                (not (issue lostPerson))
                )))
                
                
                

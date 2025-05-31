import Database_emotion as db
import Database_user as db_user
import Database_alerts as db_alert
import Analysis as magic

def send(PatientName,TimeInsec):
    NumberOfEMoition = TimeInsec//5 
    direction =magic.DirectionAlerts(PatientName ,NumberOfEMoition)
    if direction == 'decreasing':
        message = "Mr or Mrs "+PatientName+" has been in bad mood for the last "+str(TimeInsec//60)+" min please check him/her as soon as possible."
            
        db_alert.save(PatientName , message )
           
        
def getAlerts(PatientName):
    return db_alert.getAlerts(PatientName)


            
        
        
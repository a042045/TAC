import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Encontrar angulo
        
def calculate_angle(a, b, c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
            
    radians = np.arctan2(c[1]-b[1], c[0]-c[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle  = np.abs(radians*180.0/np.pi)
            
    if angle > 180.0:
        angle = 360-angle
                
    return angle

#Iniciar o programa
cap = cv2.VideoCapture(0)

counter = 0
stage = None

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        #Cor para RGB
        image =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        #Deteção
        results = pose.process(image)
        
        #Cor para BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extrair as landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Cordenadas
            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            
            # Calcular angulo
            angle = calculate_angle(hip, knee, ankle)
            
            # Visualizar angulo
            cv2.putText(image, str(angle),
                            tuple(np.multiply(knee, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )
            
            # logica agachamento
            if angle > 160:
                stage = "up"
            if angle < 60 and stage =='up':
                stage="down"
                counter +=1
                print(counter)
            
        except:
            pass
        
        # Desenho box
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        
        # Contagem
        cv2.putText(image, 'REPS', (15,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter),
                    (10,60),
                     cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        
        # Desenho das deteções
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)                                  
                                  )
        
        cv2.imshow('Mediapipe Feed', image)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
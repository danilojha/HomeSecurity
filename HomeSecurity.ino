#define trigPin 9
#define echoPin 8

void setup(){
  
   Serial.begin(115200);
   system("ifconfig eth0 169.254.1.1 netmask 255.255.0.0 up");
  system("ssh");
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop(){
    system("ifconfig > /dev/ttyGS0 2>&1");
 if (distance() < 50){
  system("/home/root/Stalker");
  delay(5000);
   system("python /home/root/mail.py");
 }

}
double distance (){
   int duration, distance;
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(2000);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2)/29.1;
  Serial.print(distance);
  Serial.println("cm");
  delay(10);
  return distance;
}


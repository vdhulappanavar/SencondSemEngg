const int trigPin=2;
const int echoPin=4;
void setup() {
  Serial.begin(9600);
  pinMode(10 , OUTPUT);
  pinMode(11 , OUTPUT);
  pinMode(5 , OUTPUT);
  pinMode(6 , OUTPUT);
}
float trigger()
{
   float duration;
   pinMode(trigPin , OUTPUT);
   digitalWrite(trigPin , LOW);
   delayMicroseconds(2);
   digitalWrite(trigPin , HIGH);
   delayMicroseconds(10);
   digitalWrite(trigPin , LOW);
   pinMode(echoPin , INPUT);
   duration=pulseIn(echoPin , HIGH);
   return(duration);
}
long dist()
{
  long duration, inches, cm;
  duration=trigger();
  inches=duration/74/2;
  cm=duration/29/2;
  return(cm);
}
void loop() {
 digitalWrite(10 , HIGH);
 digitalWrite(11 , LOW);
  analogWrite(6,225);
}

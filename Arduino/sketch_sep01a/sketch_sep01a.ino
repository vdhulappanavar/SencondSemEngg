void setup() {
//  Serial.print("test");
  pinMode(11 , OUTPUT);
  pinMode(10 , OUTPUT);
  pinMode(6 , OUTPUT);
  pinMode(7 , OUTPUT);
  pinMode(8 , OUTPUT);
  digitalWrite(9 , HIGH);

}

void loop() {
  digitalWrite(11 , HIGH);
  digitalWrite(10 , LOW);
  Serial.print(digitalRead(11));
  Serial.print("hello");
 // delay(1000);
 // digitalWrite(7 , LOW);
  //digitalWrite(8 , HIGH);
  analogWrite(6,255);

}

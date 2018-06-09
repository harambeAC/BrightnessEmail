int sensePin = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(sensePin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = analogRead(sensePin);
  Serial.println(value);
  delay(10000);
}

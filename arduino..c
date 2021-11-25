String x;
void setup() {
    Serial.begin(9600);
    delay(2000);
}

void loop() {
    if (Serial.available()) {
         x = Serial.readString();
         
         Serial.print(x + "\n");
         //Serial.print("%s\n",x);
         //Serial.print("\n");
         //Serial.readStringUntil('\n');
    }
}

// Copyright (c) Sandeep Mistry. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.

#include <CAN.h>

void setup() {
  Serial.begin(115200);
  while (!Serial);

  Serial.println("CAN Receiver");

  // start the CAN bus at 500 kbps
  if (!CAN.begin(500E3)) {
    Serial.println("Starting CAN failed!");
    while (1);
  }
}

void loop() {
  // try to parse packet
  int packetSize = CAN.parsePacket();

  if (packetSize) {
    Serial.print(millis()/1000.0);
    Serial.print(" ");
    
    Serial.print(CAN.packetId(), HEX);

    if (CAN.packetExtended())    // received a packet
      Serial.print(" EXT");

    if (CAN.packetRtr()) { // Remote transmission request, packet contains no data
      Serial.print(" RTR ");
      Serial.print(CAN.packetDlc());
    } else {
      //Serial.println(packetSize);
      while (CAN.available()) {
        Serial.print(" ");
        Serial.print((int)CAN.read(), HEX);
      }
    }

    Serial.println();
  }
}

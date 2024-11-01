<style>
table td {
    padding: .5rem !important;
}

div.mqtt-topic {
    display: flex;
    align-items: center;
}

div.mqtt-topic div:first-child span {
    --padding-right: .5rem;
    min-width: calc(var(--md-icon-size) + var(--padding-right));
    padding-right: var(--padding-right);
}

div.mqtt-topic > div:last-child {
    line-height: 1.1;
    font-size: .6rem;
}

div.mqtt-topic > div:last-child > span:not(:last-child)::after {
    content: " ";
    display: block;
}

div.mqtt-topic > div:last-child > span {
    font-family: monospace;
    padding-left: calc(0.25rem * var(--idx));
}
</style>

# MQTT Topics

## How to Read

* The base topic, as configured in the web GUI, is a prefix to all topics.
* Topics with an eye icon :material-eye: are to be read by the user, as
  OpenDTU-OnBattery publishes to these topics.
* Topics with a pencil icon :material-pencil: are to be written by the user, as
  OpenDTU-OnBattery subscribes to these topics.

## General topics

| Topic                            | Description                                              | Value / Unit               |
| -------------------------------- | -------------------------------------------------------- | -------------------------- |
| {{ mqttr("dtu/ip") }}            | IP address of OpenDTU-OnBattery                          | IP address                 |
| {{ mqttr("dtu/hostname") }}      | Current hostname of the dtu (as set in web GUI)          |                            |
| {{ mqttr("dtu/rssi") }}          | Wi-Fi network quality                                    | db value                   |
| {{ mqttr("dtu/status") }}        | Indicates whether OpenDTU-OnBattery network is reachable | online /  offline          |
| {{ mqttr("dtu/temperature") }}   | Temperature of the ESP32                                 | °C                         |
| {{ mqttr("dtu/uptime") }}        | Time in seconds since startup                            | seconds                    |
| {{ mqttr("dtu/heap/free") }}     | Available heap                                           | Bytes                      |
| {{ mqttr("dtu/heap/size") }}     | Total heap size                                          | Bytes                      |
| {{ mqttr("dtu/heap/minfree") }}  | Lowest level of free heap since boot                     | Bytes                      |
| {{ mqttr("dtu/heap/maxalloc") }} | Largest block of heap that can be allocated at once      | Bytes                      |

## Inverter total topics

Enabled inverter means, that only inverters with "Poll inverter data" enabled are considered.

| Topic                         | Description                                     | Value / Unit |
| ------------------------------| ------------------------------------------------| ------------ |
| {{ mqttr("ac/power") }}       | Sum of AC active power of all enabled inverters | Watt (W) |
| {{ mqttr("ac/yieldtotal") }}  | Sum of energy converted to AC since reset watt hours of all enabled inverters | Kilo watt hours (kWh) |
| {{ mqttr("ac/yieldday") }}    | Sum of energy converted to AC per day in watt hours of all enabled inverters | Watt hours (Wh)
| {{ mqttr("ac/is_valid") }}    | Indicator whether all enabled inverters where reachable | 0 or 1 |
| {{ mqttr("dc/power") }}       | Sum of DC power of all enabled inverters | Watt (W) |
| {{ mqttr("dc/irradiation") }} | Produced power of all enabled inverter stripes with defined irradiation settings divided by sum of all enabled inverters irradiation | % |
| {{ mqttr("dc/is_valid") }}    | Indicator whether all enabled inverters where reachable | 0 or 1 |

## Inverter specific topics

serial will be replaced with the serial number of the inverter.

| Topic                                            | Description                                          | Value / Unit               |
| ------------------------------------------------ | ---------------------------------------------------- | -------------------------- |
| {{ mqttr("[serial]/name") }}                     | Name of the inverter as configured in web GUI        |                            |
| {{ mqttr("[serial]/device/bootloaderversion") }} | Bootloader version of the inverter                   |                            |
| {{ mqttr("[serial]/device/fwbuildversion") }}    | Firmware version of the inverter                     |                            |
| {{ mqttr("[serial]/device/fwbuilddatetime") }}   | Build date / time of inverter firmware               |                            |
| {{ mqttr("[serial]/device/hwpartnumber") }}      | Hardware part number of the inverter                 |                            |
| {{ mqttr("[serial]/device/hwversion") }}         | Hardware version of the inverter                     |                            |
| {{ mqttr("[serial]/radio/tx_request") }}         | Amount of sent packet requests                       |                            |
| {{ mqttr("[serial]/radio/tx_re_request") }}      | Amount of sent fragment resend requests              |                            |
| {{ mqttr("[serial]/radio/rx_success") }}         | Amount of successfull received packets               |                            |
| {{ mqttr("[serial]/radio/rx_fail_nothing") }}    | Amount of failed packets, nothing was received       |                            |
| {{ mqttr("[serial]/radio/rx_fail_partial") }}    | Amount of failed packets, some fragments where missing |                          |
| {{ mqttr("[serial]/radio/rx_fail_corrupt") }}    | Amount of failed packets, payload corrupt            |                            |
| {{ mqttr("[serial]/radio/rssi") }}               | RSSI of last received packet (Inverters with NRF24 module only support 2 states. > -64dBm and < -64dBm. In the first case -30 dBm is shown, in the second one -80 dBm) | dBm                        |
| {{ mqttr("[serial]/status/reachable") }}         | Indicates whether the inverter is reachable          | 0 or 1                     |
| {{ mqttr("[serial]/status/producing") }}         | Indicates whether the inverter is producing AC power | 0 or 1                     |
| {{ mqttr("[serial]/status/last_update") }}       | Unix timestamp of last inverter statistics udpate    | seconds since JAN 01 1970 (UTC) |

### AC channel / global specific topics

| Topic                                     | Description                                          | Value / Unit               |
| ----------------------------------------- | ---------------------------------------------------- | -------------------------- |
| {{ mqttr("[serial]/0/current") }}         | AC current in ampere                                 | Ampere (A)                 |
| {{ mqttr("[serial]/0/efficiency") }}      | Ratio AC Power over DC Power in percent              | %                          |
| {{ mqttr("[serial]/0/frequency") }}       | AC frequency in hertz                                | Hertz (Hz)                 |
| {{ mqttr("[serial]/0/power") }}           | AC active power in watts                             | Watt (W)                   |
| {{ mqttr("[serial]/0/powerdc") }}         | DC power in watts                                    | Watt (W)                   |
| {{ mqttr("[serial]/0/powerfactor") }}     | Power factor in percent                              | %                          |
| {{ mqttr("[serial]/0/reactivepower") }}   | AC reactive power in VAr                             | VAr                        |
| {{ mqttr("[serial]/0/temperature") }}     | Temperature of inverter in degree celsius            | Degree Celsius (°C)        |
| {{ mqttr("[serial]/0/voltage") }}         | AC voltage in volt                                   | Volt (V)                   |
| {{ mqttr("[serial]/0/yieldday") }}        | Energy converted to AC per day in watt hours         | Watt hours (Wh)            |
| {{ mqttr("[serial]/0/yieldtotal") }}      | Energy converted to AC since reset watt hours        | Kilo watt hours (kWh)      |

### DC input channel topics

[1-4] represents the different inputs. The amount depends on the inverter model.

| Topic                                     | Description                                          | Value / Unit               |
| ----------------------------------------- | ---------------------------------------------------- | -------------------------- |
| {{ mqttr("[serial]/[1-4]/current") }}     | DC current of specific input in ampere               | Ampere (A)                 |
| {{ mqttr("[serial]/[1-4]/name") }}        | Name of the DC input channel as configured in web GUI|                            |
| {{ mqttr("[serial]/[1-4]/irradiation") }} | Ratio DC Power over set maximum power (in web GUI)   | %                          |
| {{ mqttr("[serial]/[1-4]/power") }}       | DC power of specific input in watt                   | Watt (W)                   |
| {{ mqttr("[serial]/[1-4]/voltage") }}     | DC voltage of specific input in volt                 | Volt (V)                   |
| {{ mqttr("[serial]/[1-4]/yieldday") }}    | Energy converted to AC per day on specific input     | Watt hours (Wh)            |
| {{ mqttr("[serial]/[1-4]/yieldtotal") }}  | Energy converted to AC since reset on specific input | Kilo watt hours (kWh)      |

### Inverter limit specific topics

cmd topics are used to set values. Status topics are updated from values set in the inverter.

| Topic                                                    | Description                                          | Value / Unit               |
| -------------------------------------------------------- | ---------------------------------------------------- | -------------------------- |
| {{ mqttr("[serial]/status/limit_relative") }}            | Current applied production limit of the inverter     | % of total possible output |
| {{ mqttr("[serial]/status/limit_absolute") }}            | Current applied production limit of the inverter     | Watt (W)                   |
| {{ mqttw("[serial]/cmd/limit_persistent_relative") }}    | Set the inverter limit as a percentage of total production capability. The  value will survive the night without power. The updated value will show up in the web GUI and limit_relative topic immediatly. | %                          |
| {{ mqttw("[serial]/cmd/limit_persistent_absolute") }}    | Set the inverter limit as a absolute value. The  value will survive the night without power. The updated value will set immediatly within the inverter but show up in the web GUI and limit_relative topic after around 4 minutes. If you are using a already known inverter (known Hardware ID), the updated value will show up within a few seconds. | Watt (W)                   |
| {{ mqttw("[serial]/cmd/limit_nonpersistent_relative") }} | Set the inverter limit as a percentage of total production capability. The  value will reset to the last persistent value at night without power. The updated value will show up in the web GUI and limit_relative topic immediatly. The value must be published non-retained, otherwise it will be ignored! | %                          |
| {{ mqttw("[serial]/cmd/limit_nonpersistent_absolute") }} | Set the inverter limit as a absolute value. The  value will reset to the last persistent value at night without power. The updated value will set immediatly within the inverter but show up in the web GUI and limit_relative topic after around 4 minutes. If you are using a already known inverter (known Hardware ID), the updated value will show up within a few seconds. The value must be published non-retained, otherwise it will be ignored! | Watt (W)                   |
| {{ mqttw("[serial]/cmd/power") }}                        | Turn the inverter on (1) or off (0)                 | 0 or 1                     |
| {{ mqttw("[serial]/cmd/reset_rf_stats") }}               | Reset the radio statistics                          | 1                          |
| {{ mqttw("[serial]/cmd/restart") }}                      | Restarts the inverters (also resets YieldDay)       | 1                          |

## Victron MPPT topics

### General

| Topic                                | Description                                          | Value / Unit               |
| -------------------------------------| ---------------------------------------------------- | -------------------------- |
| {{ mqttr("victron/[serial]/PID") }}  | Product description                                  | text                       |
| {{ mqttr("victron/[serial]/SER") }}  | Serial number                                        | text                       |
| {{ mqttr("victron/[serial]/FW") }}   | Firmware number                                      | int                        |
| {{ mqttr("victron/[serial]/LOAD") }} | Load output state                                    | ON /  OFF                  |
| {{ mqttr("victron/[serial]/CS") }}   | State of operation                                   | text, e.g., "Bulk"         |
| {{ mqttr("victron/[serial]/ERR") }}  | Error code                                           | text, e.g., "No error"     |
| {{ mqttr("victron/[serial]/OR") }}   | Off reasen                                           | text, e.g., "Not off"      |
| {{ mqttr("victron/[serial]/MPPT") }} | Tracker operation mode                               | text, e.g., "MPP Tracker active" |
| {{ mqttr("victron/[serial]/HSDS") }} | Day sequence number (0...364)                        | int in days                |

### Battery output

| Topic                             | Description                                          | Value / Unit               |
| ----------------------------------| ---------------------------------------------------- | -------------------------- |
| {{ mqttr("victron/[serial]/V") }} | Voltage                                              | Volt (V)                   |
| {{ mqttr("victron/[serial]/I") }} | Current                                              | Ampere (A)                 |

### Solar input

| Topic                               | Description                                          | Value / Unit               |
| ----------------------------------- | ---------------------------------------------------- | -------------------------- |
| {{ mqttr("victron/[serial]/VPV") }} | Voltage                                              | Volt (V)                   |
| {{ mqttr("victron/[serial]/PPV") }} | Power                                                | Watt (W)                   |
| {{ mqttr("victron/[serial]/H19") }} | Yield total (user resettable counter)                | Kilo watt hours (kWh)      |
| {{ mqttr("victron/[serial]/H20") }} | Yield today                                          | Kilo watt hours (kWh)      |
| {{ mqttr("victron/[serial]/H21") }} | Maximum power today                                  | Watt (W)                   |
| {{ mqttr("victron/[serial]/H22") }} | Yield yesterday                                      | Kilo watt hours (kWh)      |
| {{ mqttr("victron/[serial]/H23") }} | Maximum power yesterday                              | Watt (W)                   |

## (Pylontech) Battery topics

!!!warning "Incomplete"
    In particular, topics specific to the JK BMS and Victron SmartShunt are not
    yet documented.

| Topic                                                      | Description                                          | Value / Unit               |
| ---------------------------------------------------------- | ---------------------------------------------------- | -------------------------- |
| {{ mqttr("battery/settings/chargeVoltage") }}              | Voltage                                              | Volt (V)                   |
| {{ mqttr("battery/settings/chargeCurrentLimitation") }}    | BMS requested max. charge current                    | Ampere (A)                 |
| {{ mqttr("battery/settings/dischargeCurrentLimitation") }} | BMS requested max. discharge current                 | Ampere (A)                 |
| {{ mqttr("battery/stateOfCharge") }}                       | State of Health                                      | %                          |
| {{ mqttr("battery/stateOfHealth") }}                       | State of Charge                                      | %                          |
| {{ mqttr("battery/dataAge") }}                             | How old the data is                                  | Seconds                    |
| {{ mqttr("battery/voltage") }}                             | Actual voltage                                       | Volt (V)                   |
| {{ mqttr("battery/current") }}                             | Actual current                                       | Ampere (A)                 |
| {{ mqttr("battery/temperature") }}                         | Actual temperature                                   | °C                         |
| {{ mqttr("battery/alarm/overCurrentDischarge") }}          | Alarm: High discharge current                        | 0 / 1                      |
| {{ mqttr("battery/alarm/underTemperature") }}              | Alarm: Low temperature                               | 0 / 1                      |
| {{ mqttr("battery/alarm/overTemperature") }}               | Alarm: High temperature                              | 0 / 1                      |
| {{ mqttr("battery/alarm/underVoltage") }}                  | Alarm: Low voltage                                   | 0 / 1                      |
| {{ mqttr("battery/alarm/overVoltage") }}                   | Alarm: High voltage                                  | 0 / 1                      |
| {{ mqttr("battery/alarm/bmsInternal") }}                   | Alarm: BMS internal                                  | 0 / 1                      |
| {{ mqttr("battery/alarm/overCurrentCharge") }}             |                                                      |                            |
| {{ mqttr("battery/warning/highCurrentDischarge") }}        | Warning: High discharge current                      | 0 / 1                      |
| {{ mqttr("battery/warning/lowTemperature") }}              | Warning: Low temperature                             | 0 / 1                      |
| {{ mqttr("battery/warning/highTemperature") }}             | Warning: High temperature                            | 0 / 1                      |
| {{ mqttr("battery/warning/lowVoltage") }}                  | Warning: Low voltage                                 | 0 / 1                      |
| {{ mqttr("battery/warning/highVoltage") }}                 | Warning: High voltage                                | 0 / 1                      |
| {{ mqttr("battery/warning/bmsInternal") }}                 | Warning: BMS internal                                | 0 / 1                      |
| {{ mqttr("battery/manufacturer") }}                        | Manufacturer                                         | String                     |
| {{ mqttr("battery/charging/chargeEnabled") }}              | Charge enabled flag                                  | 0 / 1                      |
| {{ mqttr("battery/charging/dischargeEnabled") }}           | Discharge enabled flag                               | 0 / 1                      |
| {{ mqttr("battery/charging/chargeImmediately") }}          | Charge immediately flag                              | 0 / 1                      |

## Huawei AC charger topics

| Topic                                           | Description                                          | Value / Unit               |
| ----------------------------------------------- | ---------------------------------------------------- | -------------------------- |
| {{ mqttw("huawei/cmd/limit_online_voltage") }}  | Online voltage (i.e. CAN bus connected)              | Volt (V)                   |
| {{ mqttw("huawei/cmd/limit_online_current") }}  | Online current (i.e. CAN bus connected)              | Ampere (A)                 |
| {{ mqttw("huawei/cmd/limit_offline_voltage") }} | Offline voltage (i.e. CAN bus not connected)         | Volt (V)                   |
| {{ mqttw("huawei/cmd/limit_offline_current") }} | Offline current (i.e. CAN bus not connected)         | Ampere (A)                 |
| {{ mqttw("huawei/cmd/mode") }}                  | Controls GPIO output pin to switch slot detect       | 0 (off) / 1 (on) / 2 (set automatically depending on online_current value) / 3 (set automatically based on Power Meter reading ) |
| {{ mqttr("huawei/mode") }}                      | Currently set charging mode                          | see above                  |
| {{ mqttr("huawei/data_age") }}                  | How old the data is                                  | Seconds                    |
| {{ mqttr("huawei/input_voltage") }}             | Input voltage                                        | Volt (V)                   |
| {{ mqttr("huawei/input_current") }}             | Input current                                        | Ampere (A)                 |
| {{ mqttr("huawei/input_power") }}               | Input power                                          | Watt (W)                   |
| {{ mqttr("huawei/output_voltage") }}            | Output voltage                                       | Volt (V)                   |
| {{ mqttr("huawei/output_current") }}            | Output current                                       | Ampere (A)                 |
| {{ mqttr("huawei/max_output_current") }}        | Maximum output current (set using the online limit)  | Ampere (A)                 |
| {{ mqttr("huawei/output_power") }}              | Output power                                         | Watt (W)                   |
| {{ mqttr("huawei/input_temp") }}                | Input air temperature                                | °C                         |
| {{ mqttr("huawei/output_temp") }}               | Output air temperature                               | °C                         |
| {{ mqttr("huawei/efficiency") }}                | Efficiency                                           | Percentage                 |

## Power Limiter topics

### General

| Topic                                                       | Description                                       | Value     |
| ----------------------------------------------------------- | ------------------------------------------------- |---------- |
| {{ mqttr("powerlimiter/status/upper_power_limit") }}        | get currently set maximum power limit of inverter | Power [W] |
| {{ mqttw("powerlimiter/cmd/upper_power_limit") }}           | set maximum power limit of inverter               | Power [W] |
| {{ mqttr("powerlimiter/status/target_power_consumption") }} | get currently set target grid consumption         | Power [W] |
| {{ mqttw("powerlimiter/cmd/target_power_consumption") }}    | set target grid consumption                       | Power [W] |

### Battery Thresholds

If the inverter is solar-powered, none of the thresholds are published and
publishing to the respective `cmd` topic has no effect.

Note that, depending on your settings, some of the thresholds might have no
effect. Refer to the [DPL
documentation](https://github.com/hoylabs/OpenDTU-OnBattery/wiki/Dynamic-Power-Limiter)
to understand the thresholds.

| Topic                                                                             | Limitation |
| --------------------------------------------------------------------------------- | ---------- |
| {{ mqttr("powerlimiter/status/threshold/voltage/start") }}                        | |
| {{ mqttr("powerlimiter/status/threshold/voltage/stop") }}                         | |
| {{ mqttr("powerlimiter/status/threshold/voltage/full_solar_passthrough_start") }} | Not published if VE.Direct disabled |
| {{ mqttr("powerlimiter/status/threshold/voltage/full_solar_passthrough_stop") }}  | Not published if VE.Direct disabled |
| {{ mqttr("powerlimiter/status/threshold/soc/start") }}                            | Not published if no battery interface configured or SoC is set to be ignored |
| {{ mqttr("powerlimiter/status/threshold/soc/stop") }}                             | Not published if no battery interface configured or SoC is set to be ignored |
| {{ mqttr("powerlimiter/status/threshold/soc/full_solar_passthrough") }}           | Not published if no battery interface configured or SoC is set to be ignored or VE.Direct disabled |

All thresholds have respective `cmd` topics (replace `status` with `cmd`),
which allow to override the threshold. The overrides are persistent, i.e., new
values are written to the persistent configuration file.

Example: Use topic `powerlimiter/cmd/threshold/voltage/start` to override the
battery discharge cycle start voltage threshold.

### Mode
| Topic                                   | Description                                          | Value                      |
| --------------------------------------- | ---------------------------------------------------- | -------------------------- |
| {{ mqttw("powerlimiter/cmd/mode") }}    | Power Limiter operation mode                         | see below                  |
| {{ mqttr("powerlimiter/status/mode") }} | Get Power Limiter operation mode                     | see below                  |

Setting any a mode through MQTT has *no* effect if the Power Limiter is
disabled by configuration in the web application. The Power Limiter will stay
off in that case.

When using the web application to change DPL settings, the DPL mode will be
reset to *normal operation*.

Three modes are implemented:

* **0** - Normal operation: The Power Limiter works as configured through the
  web application.
* **1** - Fully disable with inverter shut down: The inverter is shut down and
  afterwards the Power Limiter stops operating, as if it was disabled in the
  web application. Note that this means that the inverter can start producing
  power if the web application or an MQTT topic is used to control it.
* **2** - Unconditional Full Solar-Passthrough: The power limit is set such
  that all available solar power is fed into the home, irrespective of grid
  consumption. Essentially, the inverter mimics the behavior of a traditional,
  non-smart inverter. Depending on your configuration, the inverter's limit is
  set to the following:
    1. **Inverter is powered by a battery**: The inverter's limit is set to the
       solar power output (VE.Direct interface), adjusted for efficiency, such
       that no energy from the battery is consumed. Note that if VE.Direct is
       disabled or the data is outdated, the inverter is shut down instead. This
       mode can be particularly useful in scenarios where solar power is better
       stored elsewhere, such as in an electric car.
    2. **Inverter is powered by solar modules**: The inverter's limit is set to
       the upper limit configured in the DPL settings (starting from release
       2024.05.03).

### Timeout Counter

!!!note "Availability"
    Starting from release 2024.05.03.

The DPL counts the amount of times an attempt to configure the inverter to a
particular state times out. This counter is used to decide to sent an inverter
restart command, hoping to "revive" the inverter. If the counter keeps
increasing even after multiple restart commands have been issued, the ESP
restarts as a last resort. The thresholds to perform these actions are hard
coded to 10 and 20 timeouts, respectively.

Topic `powerlimiter/status/inverter_update_timeouts` can be monitored to be
alerted by these timeouts.

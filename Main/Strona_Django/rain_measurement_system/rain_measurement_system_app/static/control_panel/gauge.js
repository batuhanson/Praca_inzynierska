const gaugeElement_water_sensor = document.getElementById("gauge_water_sensor");
const gaugeElement_rain_sensor = document.getElementById("gauge_rain_sensor");
const gaugeElement_rain_gauge = document.getElementById("gauge_rain_gauge");
function setGaugeValue_water_sensor(gauge, value, maxValue) {
  if (value < 0 || value > maxValue) {
    return;
  }

  const scaledValue = value / maxValue;
  fillgauage = document.getElementById("gauge__fill_water_sensor");
  gauagecover = document.getElementById("gauge__cover_water_sensor");
  fillgauage.style.transform = `rotate(${scaledValue / 2}turn)`;
  gauagecover.textContent = `${value}`;
}

function update_water_sensor_data() {
  $.ajax({
    url: "/water_sensor_data/",
    type: "GET",
    dataType: "json",
    success: function (data) {
      const waterSensorValue = data.get_water_sensor_data;
      setGaugeValue_water_sensor(
        gaugeElement_water_sensor,
        waterSensorValue,
        4095
      );
    },
    complete: function () {
      setTimeout(update_water_sensor_data, 5000);
    },
  });
}

function setGaugeValue_rain_sensor(gauge, value, maxValue) {
  if (value < 0 || value > maxValue) {
    return;
  }

  const scaledValue = value / maxValue;
  fillgauage = document.getElementById("gauge__fill_rain_sensor");
  gauagecover = document.getElementById("gauge__cover_rain_sensor");
  fillgauage.style.transform = `rotate(${scaledValue / 2}turn)`;
  gauagecover.textContent = `${value}`;
}

function update_rain_sensor_data() {
  $.ajax({
    url: "/rain_sensor_data/",
    type: "GET",
    dataType: "json",
    success: function (data) {
      const rainSensorValue = data.get_rain_sensor_data;
      setGaugeValue_rain_sensor(
        gaugeElement_rain_sensor,
        rainSensorValue,
        4095
      );
    },
    complete: function () {
      setTimeout(update_rain_sensor_data, 5000);
    },
  });
}

function setGaugeValue_rain_gauge(gauge, value, maxValue) {
  if (value < 0 || value > maxValue) {
    return;
  }

  const scaledValue = value / maxValue;
  fillgauage = document.getElementById("gauge__fill_rain_gauge");
  gauagecover = document.getElementById("gauge__cover_rain_gauge");
  fillgauage.style.transform = `rotate(${scaledValue / 2}turn)`;
  gauagecover.textContent = `${value}`;
}

function update_rain_gauge_data() {
  $.ajax({
    url: "/rain_gauge_data/",
    type: "GET",
    dataType: "json",
    success: function (data) {
      const rain_gaugeSensorValue = data.get_rain_gauge_data;
      setGaugeValue_rain_gauge(
        gaugeElement_rain_gauge,
        rain_gaugeSensorValue,
        100
      );
    },
    complete: function () {
      setTimeout(update_rain_gauge_data, 5000);
    },
  });
}

update_water_sensor_data();
update_rain_sensor_data();
update_rain_gauge_data();

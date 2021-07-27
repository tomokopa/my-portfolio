var sound_count = 0;
var notification_count = 0;
var button_count = 0;

var sound_sw = document.getElementById("sound_swith");
var notification_sw = document.getElementById("notification_swith");
var min_dis = document.getElementById("min_display");
var sec_dis = document.getElementById("sec_display");
var start_stop_btn = document.getElementById("start_stop_button");
var reset_btn = document.getElementById("reset_button");

// sound_switchの関数
sound_sw.onchange = () => {
  sound_count ++;
  console.log('sound_count:', sound_count)
};

// notification_swithの関数
notification_sw.onchange = () => {
  notification_count ++;
  console.log('notification_count:', notification_count)

  if (notification_count % 2 === 1) {
    notification_fnc("通知 : ON", 3000);
  }
};

// start_stop_buttonの関数
start_stop_btn.onclick = () => {
  let base = performance.now();

  min_int = integer(min_dis);
  sec_int = integer(sec_dis);

  if (min_int === 0 && sec_int === 0) {
    console.log('input integer.');
    return;
  } else {
    button_count ++;
  }

  if (button_count % 2 === 1) {
    console.log('button_count = Odd:', button_count);

    console.log('start')
    start_stop_btn.textContent = "stop";
    reset_btn.disabled = true;

    let count = min_int * 60 + sec_int;

    if (button_count === 1) {
      min_dis.disabled = true;
      sec_dis.disabled = true;
    }

    timer(count, base);

  } else {
    console.log('button_count = Even:', button_count)

    start_stop_btn.disabled = true;
    reset_btn.disabled = true;
  }
};

// reset_buttonの関数
reset_btn.onclick = () => {
  console.log('reset');
  min_sec_display(0);
  display_abled();
};


// inputされた要素を整数化する関数
let integer = (time_element) => {
  if (time_element.value === '') {
    return 0;
  } else {
    return parseInt(time_element.value);
  }
};

// timer関数
let timer = async (count_time, base_time)=> {
  await countdown(count_time, base_time);

  start_stop_btn.textContent = 'start';
  start_stop_btn.removeAttribute('disabled');
  reset_btn.removeAttribute('disabled');

  finish_time = performance.now();
  console.log('total_time:', finish_time - base_time);
};

// countdown関数
let countdown = async (count_time, base_time) => {
  let last_time = 0;

  for (var i = count_time; i >= 0; i--) {
    if (button_count % 2 === 0) {
      console.log('stop');
      return ;
    } else if (i > 0) {

      if (i !== count_time){
        min_sec_display(i)
      }

      console.log('i > 0:', i);
      let now_time= performance.now();
      let sleep_time = (1000 - (now_time - base_time) % 1000) || 1000;

      // sleep_timeのエラー対策
      if (sleep_time < 1) {
        console.error('error. sleep_time :', sleep_time, 'changed to 1000');
        sleep_time = 1000;
      }

      await sleep(sleep_time);

      // consoleでの確認用
      console.log('now_time :', now_time);
      console.log('sleep_time :', sleep_time);

      let interval_time = now_time - last_time;

      if (i === count_time) {
        ;
      } else if (interval_time < 1025 && interval_time > 975) {
        console.log('interval_time :', interval_time);
      } else {
        // interval_timeのエラー表示(現状、対策不可)
        // choromeのタブの切り替えが原因か。
        console.error('eroor. interval_time :', interval_time);
      }

      last_time = now_time;
      // consoleでの確認用　ここまで

    } else {
      min_sec_display(i)
      console.log('i = 0:', i);
      display_abled();

      if (notification_count % 2 === 1) {
        notification_fnc("It's time.", 10 * 60 * 1000);
      }

      if (sound_count % 2 === 0) {
        document.getElementById("sound").play();
      }

    }
  }
};

// sleep関数(一定時間処理を止める関数)
let sleep = time => new Promise(resolve => setTimeout(resolve, time));

// 秒のみから、分・秒表示に戻す関数
let min_sec_display = (time) => {
  min_dis.value = (time/60|0);
  sec_dis.value = (time%60);
};

// displayへの入力を可能にする関数
const display_abled = () => {
  button_count = 0;
  min_dis.removeAttribute('disabled');
  sec_dis.removeAttribute('disabled');
};

// 通知内容についての関数
let notification_fnc = (comment, timeout_time)=> {
  Push.create("Push Timer", {
    body : comment,
    timeout : timeout_time,
    onClick : function () {
      this.close();
    }
  });
};
function activateBoost() {
    let link = document.getElementById('linkInput').value;
    let status = document.getElementById('status-panel');
    
    status.innerHTML = "🚀 J5 سرور سے کنیکٹ ہو رہا ہے...";
    
    setTimeout(() => {
        status.innerHTML = "✅ کنکشن کامیاب! 1 ملین بوسٹ آپ کے چینل پر بھیجے جا رہے ہیں...";
    }, 2000);
}
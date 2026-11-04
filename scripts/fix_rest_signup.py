import re
import shutil

app_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/js/app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Fix the broken signUp block
broken_block = """        if (authRes.ok) {
          const authData = await authRes.json();
          idToken = authData.idToken;
          break;
        } else {
          try {
            const errData = await authRes.json();
            const errMsg = errData.error && errData.error.message;
            if (errMsg === 'EMAIL_NOT_FOUND') {
              const signUpUrl = ;
              const signUpRes = await fetch(signUpUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                  email: ,
                  password: ,
                  returnSecureToken: true
                })
              });
              if (signUpRes.ok) {
                const signUpData = await signUpRes.json();
                idToken = signUpData.idToken;
                break;
              }
            }
          } catch(errJson) {}
        }"""

clean_block = """        if (authRes.ok) {
          const authData = await authRes.json();
          idToken = authData.idToken;
          break;
        } else {
          try {
            const errData = await authRes.json();
            const errMsg = errData.error && errData.error.message;
            if (errMsg === 'EMAIL_NOT_FOUND') {
              const signUpUrl = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=" + API_KEY;
              const signUpRes = await fetch(signUpUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                  email: studentId.toLowerCase() + "@haku.local",
                  password: "haku_" + p + "_sec",
                  returnSecureToken: true
                })
              });
              if (signUpRes.ok) {
                const signUpData = await signUpRes.json();
                idToken = signUpData.idToken;
                break;
              }
            }
          } catch(errJson) {}
        }"""

assert broken_block in code, "broken_block not found"
code = code.replace(broken_block, clean_block)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(code)

pub_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/public/js/app.js'
shutil.copy2(app_path, pub_path)
print("Fixed syncStudentViaRest in js/app.js and public/js/app.js!")

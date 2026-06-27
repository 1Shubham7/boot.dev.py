#!/usr/bin/env bash
# Verify every lesson: the complete solution must PASS all cases,
# and the incomplete starter must FAIL. Boot.dev runs the student's
# file as `main.py`, and test_main.py does `from main import ...`,
# so we swap each solution into a temp main.py and run the tests.
#
# Usage:  ./verify.sh            # check every lesson with a test_main.py
#         ./verify.sh enumerate  # check only matching lesson dir(s)

set -u
filter="${1:-}"
overall_ok=1

# Find every lesson dir that has a test_main.py (skip the reference/ pack)
while IFS= read -r testfile; do
  dir="$(dirname "$testfile")"
  case "$dir" in */reference/*|reference/*) continue;; esac
  if [ -n "$filter" ] && [[ "$dir" != *"$filter"* ]]; then continue; fi

  echo "=================================================="
  echo "LESSON: $dir"
  echo "=================================================="

  tmp="$(mktemp -d)"
  cp "$dir/test_main.py" "$tmp/test_main.py"

  # 1) COMPLETE solution -> should PASS
  cp "$dir/complete_main.py" "$tmp/main.py"
  out_complete="$(cd "$tmp" && python3 test_main.py 2>&1)"
  if echo "$out_complete" | grep -q "===== PASS\|= PASS ="; then
    echo "  [complete_main.py] PASS  ✅   ($(echo "$out_complete" | tail -1))"
  else
    echo "  [complete_main.py] DID NOT PASS  ❌"
    echo "$out_complete" | tail -3 | sed 's/^/      /'
    overall_ok=0
  fi

  # 2) INCOMPLETE starter -> should FAIL (or error out)
  cp "$dir/incomplete_main.py" "$tmp/main.py"
  out_incomplete="$(cd "$tmp" && python3 test_main.py 2>&1)"
  if echo "$out_incomplete" | grep -q "= FAIL =" || ! echo "$out_incomplete" | grep -q "= PASS ="; then
    echo "  [incomplete_main.py] FAILS as expected  ✅"
  else
    echo "  [incomplete_main.py] UNEXPECTEDLY PASSED  ❌  (starter gives away the answer!)"
    overall_ok=0
  fi

  rm -rf "$tmp"
  echo ""
done < <(find . -name test_main.py | sort)

echo "=================================================="
if [ "$overall_ok" -eq 1 ]; then
  echo "ALL LESSONS OK ✅"
else
  echo "SOME CHECKS FAILED ❌"
  exit 1
fi

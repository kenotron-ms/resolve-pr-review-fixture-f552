"""Deterministic review-result producer used only as a host-boundary test double."""
import json, subprocess, sys
scenario = json.load(open('.review-scenario.json'))
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
mode = scenario['mode']
if mode == 'missing':
    sys.exit(0)
if mode == 'oversized_file':
    result = {'version': 1, 'repository': scenario['repository'], 'pr_number': scenario['pr_number'], 'head_sha': head,
              'conclusion': 'success', 'title': 'oversized file', 'summary': 'padded', 'text': 'x'}
    open(sys.argv[1], 'w').write(json.dumps(result) + ' ' * 70000)
    sys.exit(0)
if mode == 'oversized_field':
    result = {'version': 1, 'repository': scenario['repository'], 'pr_number': scenario['pr_number'], 'head_sha': head,
              'conclusion': 'success', 'title': 'oversized field', 'summary': 'ok', 'text': 'x' * 32001}
    open(sys.argv[1], 'w').write(json.dumps(result))
    sys.exit(0)
if mode == 'limit_max':
    result = {'version': 1, 'repository': scenario['repository'], 'pr_number': scenario['pr_number'], 'head_sha': head,
              'conclusion': 'neutral', 'title': 't' * 200, 'summary': 's' * 16000, 'text': 'x' * 32000}
    open(sys.argv[1], 'w').write(json.dumps(result))
    sys.exit(0)
if mode == 'malformed':
    open(sys.argv[1], 'w').write('{"version": 1, "repository": ')
    sys.exit(0)
result = {'version': 1, 'repository': scenario['repository'], 'pr_number': scenario['pr_number'],
          'head_sha': ('0' * 40) if mode == 'mismatch_head' else head,
          'conclusion': scenario['conclusion'], 'title': scenario['title'],
          'summary': 'Deterministic fixture verdict: ' + scenario['title'], 'text': 'stub review text for ' + head}
open(sys.argv[1], 'w').write(json.dumps(result))

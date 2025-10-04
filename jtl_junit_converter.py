# scripts/jtl_junit_converter.py
# 用法：python3 jtl_junit_converter.py <input_jtl_xml> <output_junit_xml>
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

def is_success(sample):
    # JMeter JTL XML：s="true/false"；rc="200" 等
    s = sample.get('s', 'true').lower() == 'true'
    rc = sample.get('rc', '')
    return s and rc.isdigit() and 200 <= int(rc) < 300

def ms_to_seconds(ms):
    try:
        return float(ms) / 1000.0
    except:
        return 0.0

def main(inp, outp):
    tree = ET.parse(inp)
    root = tree.getroot()  # <testResults>
    # JUnit 根
    ts = ET.Element('testsuite', {
        'name': 'JMeter Suite',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    })

    total = 0
    failures = 0
    time_sum = 0.0

    for sample in root:
        if sample.tag not in ('sample', 'httpSample'):
            continue
        total += 1

        label = sample.get('lb', sample.get('tn', 'sample'))
        elapsed = ms_to_seconds(sample.get('t', '0'))
        time_sum += elapsed

        tc = ET.SubElement(ts, 'testcase', {
            'classname': 'JMeter',
            'name': label,
            'time': str(elapsed)
        })

        if not is_success(sample):
            failures += 1
            rc = sample.get('rc', '')
            rm = sample.get('rm', '')
            ET.SubElement(tc, 'failure', {
                'message': f'HTTP {rc} {rm}'
            }).text = (sample.findtext('responseData') or '').strip()[:1000]

    ts.set('tests', str(total))
    ts.set('failures', str(failures))
    ts.set('errors', '0')
    ts.set('time', str(round(time_sum, 3)))

    junit = ET.Element('testsuites')
    junit.append(ts)
    ET.ElementTree(junit).write(outp, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: jtl_junit_converter.py <input_jtl_xml> <output_junit_xml>')
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])


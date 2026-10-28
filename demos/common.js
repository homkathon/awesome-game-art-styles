// Shared test scene for the style demos: a small village on an island, built from primitives so it needs no assets.
// Every demo uses the same scene and camera; only materials and post-processing change.
import * as THREE from 'three';

export const PALETTE = {
  sky: '#9fd3f0', grass: '#7bc86c', sand: '#e9d39a', water: '#3a8fd1', wall: '#f2e6d0',
  roof: '#d9534f', roof2: '#4a78c2', trunk: '#8a5a33', leaf: '#3f9b4a', stone: '#9aa0a6', body: '#f2b134', head: '#ffd9b3',
};

// A small procedural checker so texture effects (affine warping, filtering) are visible.
export function checkerTexture(a = '#ffffff', b = '#d8d8d8', n = 8) {
  const c = document.createElement('canvas');
  c.width = c.height = 64;
  const g = c.getContext('2d');
  const s = 64 / n;
  for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) { g.fillStyle = (x + y) % 2 ? a : b; g.fillRect(x * s, y * s, s, s); }
  const t = new THREE.CanvasTexture(c);
  t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.magFilter = THREE.NearestFilter;
  t.colorSpace = THREE.SRGBColorSpace;
  return t;
}

// Build the scene. makeMaterial(color, opts) lets each style supply its own material; opts.textured marks surfaces
// that carry the checker texture.
export function buildScene(makeMaterial) {
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(PALETTE.sky);
  const root = new THREE.Group();
  scene.add(root);
  const add = (geo, color, pos, opts = {}) => {
    const m = new THREE.Mesh(geo, makeMaterial(color, opts));
    m.position.set(...pos);
    if (opts.rot) m.rotation.set(...opts.rot);
    m.castShadow = m.receiveShadow = true;
    root.add(m);
    return m;
  };

  add(new THREE.CylinderGeometry(9, 9, 0.4, 48), PALETTE.water, [0, -0.6, 0]);
  add(new THREE.CylinderGeometry(6, 6.6, 1, 40), PALETTE.sand, [0, -0.3, 0]);
  add(new THREE.CylinderGeometry(5.4, 5.8, 0.4, 40), PALETTE.grass, [0, 0.3, 0], { textured: true });

  const house = (x, z, roof, s = 1) => {
    add(new THREE.BoxGeometry(1.6 * s, 1.2 * s, 1.4 * s), PALETTE.wall, [x, 0.5 + 0.6 * s, z], { textured: true });
    add(new THREE.ConeGeometry(1.25 * s, 0.9 * s, 4), roof, [x, 0.5 + 1.65 * s, z], { rot: [0, Math.PI / 4, 0] });
    add(new THREE.BoxGeometry(0.35 * s, 0.6 * s, 0.05), PALETTE.trunk, [x, 0.5 + 0.3 * s, z + 0.72 * s]);
  };
  house(-1.8, -1.2, PALETTE.roof, 1.1);
  house(1.6, -2.0, PALETTE.roof2, 0.9);
  house(2.6, 0.9, PALETTE.roof, 0.8);

  const tree = (x, z, h = 1) => {
    add(new THREE.CylinderGeometry(0.12, 0.16, 0.8 * h, 8), PALETTE.trunk, [x, 0.5 + 0.4 * h, z]);
    add(new THREE.IcosahedronGeometry(0.6 * h, 0), PALETTE.leaf, [x, 0.5 + 1.1 * h, z]);
  };
  [[-3.6, 1.2, 1.2], [-3.0, 2.6, 0.9], [-0.4, -3.6, 1.1], [3.9, -1.6, 1], [0.8, 3.3, 0.8]].forEach(t => tree(...t));

  add(new THREE.DodecahedronGeometry(0.5, 0), PALETTE.stone, [-0.6, 0.75, 2.4]);
  add(new THREE.TorusKnotGeometry(0.45, 0.15, 96, 12), PALETTE.roof2, [0.4, 1.6, 0.6]);

  // a little character
  const hero = new THREE.Group();
  hero.position.set(-0.2, 0.5, 0.4);
  root.add(hero);
  const body = new THREE.Mesh(new THREE.CapsuleGeometry(0.28, 0.4, 4, 12), makeMaterial(PALETTE.body, {}));
  body.position.y = 0.5;
  const head = new THREE.Mesh(new THREE.SphereGeometry(0.26, 20, 14), makeMaterial(PALETTE.head, {}));
  head.position.y = 1.05;
  for (const m of [body, head]) { m.castShadow = m.receiveShadow = true; hero.add(m); }

  const sun = new THREE.DirectionalLight('#fff4e0', 2.6);
  sun.position.set(6, 10, 4);
  sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048);
  Object.assign(sun.shadow.camera, { left: -8, right: 8, top: 8, bottom: -8 });
  scene.add(sun, new THREE.HemisphereLight('#dff1ff', '#6b5a3a', 1.1));

  return { scene, root, hero, sun };
}

export function makeCamera(aspect) {
  const camera = new THREE.PerspectiveCamera(35, aspect, 0.5, 100);
  return camera;
}

const params = new URLSearchParams(location.search);

// Slow orbit plus a hopping character, so every style is judged in motion (shimmer, swimming textures, dither crawl).
// ?t=<seconds> freezes the animation at that time (used for the README images).
export function animate(camera, hero, t) {
  if (params.has('t')) t = Number(params.get('t'));
  const a = t * 0.15;
  camera.position.set(Math.sin(a) * 15, 9, Math.cos(a) * 15);
  camera.lookAt(0, 0.8, 0);
  hero.position.y = 0.5 + Math.abs(Math.sin(t * 3)) * 0.35;
  hero.rotation.y = t;
}

// Small header with the style name and a link back to its page. ?bare hides it.
export function label(name, page) {
  if (params.has('bare')) return;
  const d = document.createElement('div');
  d.innerHTML = `<b>${name}</b> · <a href="${page}">style page</a> · <a href="./">all demos</a>`;
  Object.assign(d.style, { position: 'fixed', left: '12px', top: '10px', font: '14px system-ui, sans-serif', color: '#fff', background: 'rgba(0,0,0,.55)', padding: '6px 10px', borderRadius: '6px' });
  for (const a of d.querySelectorAll('a')) a.style.color = '#9fd3ff';
  document.body.appendChild(d);
}
